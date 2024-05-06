import numpy as np


class Processor(object):

    def __init__(self, video_reader):
        self.data = video_reader.get_data

    def arm_analytics(self):
        """
        calculates average arm angle difference from ideal 90 degrees for right and left arms
        :return: dictionary containing average right and left arm angle difference from 90 degrees
        """
        n = len(data['right_shoulder'])
        right_arm_angle_difference = 0
        left_arm_angle_difference = 0
        for i in range(n):
            right_arm_angle_difference += Processor.__arm_angle_difference(self.data['right_shoulder'][i],
                                                                           self.data['right_elbow'][i],
                                                                           self.data['right_wrist'][i])
            left_arm_angle_difference += Processor.__arm_angle_difference(self.data['left_shoulder'][i],
                                                                          self.data['left_elbow'][i],
                                                                          self.data['left_wrist'][i])
        right_arm_angle_difference /= n
        left_arm_angle_difference /= n
        return {'right arm angle difference': right_arm_angle_difference,
                'left arm angle difference': left_arm_angle_difference}

    def feet_analytics(self):
        """
        calculates average back leg angle difference from ideal 180 degrees when leg strikes ground
        Returns: average back leg angle difference from 180 degrees when leg strikes ground, -1 if less than one stride detected
        """
        gait_duration = Processor.calculate_period(self.data['right_ankle'])
        back_leg_difference = 0
        n = 0
        for i in range(0, len(data['right_ankle']), gait_duration):
            min_y = float('-inf')
            min_index = i
            for j in range(i, i + gait_duration, 1):
                if data['right_ankle'][j][1] < min_y:
                    min_y = data['right_ankle'][j][1]
                    min_index = j
            back_leg_difference += Processor.__leg_angle_difference(self.data['right_hip'][min_index],
                                                                    self.data['right_knee'][min_index],
                                                                    self.data['right_ankle'][min_index])
            n += 1
        if n == 0:
            return -1
        back_leg_difference /= n
        return back_leg_difference

    @staticmethod
    def calculate_period(coordinates):
        """
        calculates the duration of a gait and the start of one complete gait
        models y coordinates of ankle to sine function
        :param: coordinates: list of coordinates of ankle
        :return: dictionary containing duration of gait (period) and start of one complete gait (phase)
        """
        times = numpy.array(range(len(coordinates)))
        y_coordinates = []
        for coordinate in coordinates:
            y_coordinates.append(coordinate[1])
        y_coordinates = numpy.array(y_coordinates)
        ff = numpy.fft.fftfreq(len(times), (times[1] - times[0]))
        Fyy = abs(numpy.fft.fft(y_coordinates))
        guess_frequency = abs(ff[numpy.argmax(Fyy[1:]) + 1])
        guess_amplitude = numpy.std(y_coordinates) * 2. ** 0.5
        guess_offset = numpy.mean(y_coordinates)
        guess = numpy.array([guess_amplitude, 2. * numpy.pi * guess_frequency, 0., guess_offset])

        def sine_function(t, A, w, p, c): return A * numpy.sin(w * t + p) + c

        popt, pcov = scipy.optimize.curve_fit(sine_function, times, y_coordinates, p0=guess)
        A, w, p, c = popt
        f = w / (2. * numpy.pi)
        T = 1. / f
        return T

    @staticmethod
    def __distance(p1, p2):
        """ Given points, p1 and p2, find the distance between two points
        Args:
            p1, p2 - points given as a np.array corresponding to the
            (x, y)-coordinates
        Returns:
            distance between p1 and p2
        """
        return np.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

    @staticmethod
    def __angle(p1, p2, p3):
        """Given three points, p1, p2, p3, calculate the angle formed
        Args:
            p1, p2, p3 - points given as a np.array corresponding to
            (x, y)-coordinates
        Returns:
            angle formed from the line segments formed from p1, p2, p3
        """
        vec_p1 = p1 - p2
        vec_p3 = p3 - p2
        cosine_angle = np.dot(vec_p1, vec_p3) / (np.linalg.norm(vec_p1) * np.linalg.norm(vec_p3))
        return np.arccos(cosine_angle) * (180.0 / np.pi)

    @staticmethod
    def __arm_angle_difference(shoulder, elbow, wrist):
        """
        Args:
            shoulder, elbow, wrist - points given as a np.array corresponding to
            (x, y)-coordinates
        Returns:
            the absolute difference between current arm angle and 90 degrees,
            the ideal arm angle
        """
        return abs(Processor.__angle(shoulder, elbow, wrist) - 90)

    @staticmethod
    def __leg_angle_difference(hip, knee, ankle):
        """
        Args:
            hip, knee, ankle - points given as a np.array corresponding to
            (x, y)-coordinates
        Returns:
            the absolute difference between current leg angle and 180 degrees, the ideal leg angle
        """
        # How do we determine which is the back leg? Do we have everyone face one direction?
        return abs(Processor.__angle(hip, knee, ankle) - 180)
