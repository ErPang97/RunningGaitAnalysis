from ultralytics import YOLO
import numpy, scipy.optimize
import cv2
import math


class VideoReader(object):

    def __init__(self, filename):
        self.filename = filename

    def get_data(self):
        """
        extracts keypoint data from frames of video and calculates gait data
        :return: dictionary containing list of keypoints for right and left shoulder, elbow, wrist, hip, knee, and ankle and right and left gait duration and start
        """
        # Check if there is one person in video
        if not self._detect_person:
            return None

        # Open the video file
        cap = cv2.VideoCapture(self.filename)

        # Load a pre-trained model for Pose Estimation
        model_path = "yolov8n-pose.pt"
        pose_model = YOLO(model_path)

        # Initialize dictionary for store data
        data = {'right_shoulder': [], 'right_elbow': [], 'right_wrist': [],
                'left_shoulder': [], 'left_elbow': [], 'left_wrist': [],
                'right_hip': [], 'right_knee': [], 'right_ankle': [],
                'left_hip': [], 'left_knee': [], 'left_ankle': [],
                }

        # Loop through the video frames
        while cap.isOpened():
            # Read a frame from the video
            success, frame = cap.read()

            if success:
                # Run YOLOv8 inference on the frame
                results = pose_model.model(frame)

                # Visualize the results on the frame
                annotated_frame = results[0].plot()

                # Display the annotated frame
                cv2.imshow("YOLOv8 Inference", annotated_frame)

                # Check if the keypoints attribute is present in the results
                if hasattr(results[0], 'keypoints'):
                    # Access the keypoints for the first detected object
                    keypoints = results[0].keypoints
                    # Convert keypoints to numpy array and access the keypoints for the first detected object
                    # Should only have 1 object because we only have 1 person running
                    keypoints_numpy = keypoints.xyn.cpu().numpy()[0]

                    # Add datapoints to arrays
                    data['right_shoulder'].append(keypoints_numpy[6])
                    data['right_elbow'].append(keypoints_numpy[8])
                    data['right_wrist'].append(keypoints_numpy[10])
                    data['left_shoulder'].append(keypoints_numpy[5])
                    data['left_elbow'].append(keypoints_numpy[7])
                    data['left_wrist'].append(keypoints_numpy[9])
                    data['right_hip'].append(keypoints_numpy[12])
                    data['right_knee'].append(keypoints_numpy[14])
                    data['right_ankle'].append(keypoints_numpy[16])
                    data['left_hip'].append(keypoints_numpy[11])
                    data['left_knee'].append(keypoints_numpy[13])
                    data['left_ankle'].append(keypoints_numpy[15])

                # Break the loop if 'q' is pressed
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            else:
                # Break the loop if the end of the video is reached
                break

        data['total_frames'] = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        data['fps'] = cap.get(cv2.CAP_PROP_FPS)

        # Release the video capture object and close the display window
        cap.release()
        cv2.destroyAllWindows()

        right_period_phase = self._calculate_period_phase(data['right_ankle'])
        data['right_gait_duration'] = right_period_phase['period']
        data['right_gait_start'] = right_period_phase['phase']
        left_period_phase = self._calculate_period_phase(data['left_ankle'])
        data['left_gait_duration'] = left_period_phase['period']
        data['left_gait_start'] = left_period_phase['phase']

    def _detect_person(self):
        """
        determines whether there is one person in image or video
        :return: True if there is one person in image or video, False otherwise
        """
        model = YOLO('yolov8n.pt')
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

    @staticmethod
    def _calculate_period_phase(y_coordinates):
        """
        calculates the duraction of a gait and the start of one complete gait 
        models y coordinates of ankle to sine function
        :param: y_coordinates: list of y coordinates of ankle
        :return: dictionary containing duration of gait (period) and start of one complete gait (phase)
        """
        times = numpy.array(range(0, len(y_coordinates), 1))
        y_coordinates = numpy.array(y_coordinates)
        ff = numpy.fft.fftfreq(len(times), (times[1] - times[0]))
        Fyy = abs(numpy.fft.fft(y_coordinates))
        guess_freq = abs(ff[numpy.argmax(Fyy[1:]) + 1])
        guess_amp = numpy.std(y_coordinates) * 2. ** 0.5
        guess_offset = numpy.mean(y_coordinates)
        guess = numpy.array([guess_amp, 2. * numpy.pi * guess_freq, 0., guess_offset])

        def sine_function(t, A, w, p, c): return A * numpy.sin(w * t + p) + c

        popt, pcov = scipy.optimize.curve_fit(sine_function, times, y_coordinates, p0=guess)
        A, w, p, c = popt
        f = w / (2. * numpy.pi)
        T = 1. / f
        return {'period': T, 'phase': p}
