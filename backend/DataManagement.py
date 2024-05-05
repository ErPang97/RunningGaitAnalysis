from ultralytics import YOLO
import numpy, scipy.optimize


class DataManagement(object):

    def __init__(self, filename):
        self.filename = filename

    def detect_person(self, model):
        """
        determines whether there is one person in image or video
        :return: True if there is one person in image or video, False otherwise
        """
        results = model.predict(self.filename)
        person_count = 0
        for detection in results[0]:
            if detection.names[0] == 'person':
                person_count += 1
                if person_count > 1:
                    return False
        if person_count != 1:
            return False
        return True

    def calculate_period_phase(self, time_array, y_array):
        """

        """
        time_array = numpy.array(time_array)
        y_array = numpy.array(y_array)
        ff = numpy.fft.fftfreq(len(time_array), (time_array[1] - time_array[0]))
        Fyy = abs(numpy.fft.fft(y_array))
        guess_freq = abs(ff[numpy.argmax(Fyy[1:]) + 1])
        guess_amp = numpy.std(y_array) * 2. ** 0.5
        guess_offset = numpy.mean(y_array)
        guess = numpy.array([guess_amp, 2. * numpy.pi * guess_freq, 0., guess_offset])

        def sinfunc(t, A, w, p, c):  return A * numpy.sin(w * t + p) + c

        popt, pcov = scipy.optimize.curve_fit(sinfunc, time_array, y_array, p0=guess)
        A, w, p, c = popt
        f = w / (2. * numpy.pi)
        T = 1. / f
        return {"period": T, "phase": p}
