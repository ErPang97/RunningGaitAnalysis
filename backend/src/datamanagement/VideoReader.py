import torch
from ultralytics import YOLO
import numpy as np
import cv2
import math


class VideoReader(object):

    def __init__(self, filename):
        self.filename = filename

    def get_data(self):
        """
        Extracts keypoint data from frames of video and calculates gait data.
        :return: Dictionary containing list of keypoints for right and left shoulder, elbow, wrist, hip, knee, and ankle and right and left gait duration and start.
        """
        # Check if there is one person in the video
        if not self._detect_person():
            return None

        # Open the video file
        cap = cv2.VideoCapture(self.filename)

        # Load a pre-trained model for Pose Estimation
        model_path = "yolov8n-pose.pt"
        pose_model = YOLO(model_path)

        # Initialize dictionary to store data
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
                # Convert frame to tensor
                frame_tensor = torch.from_numpy(frame)
                frame_tensor = frame_tensor.permute(2, 0, 1)  # Change to NCHW format
                frame_tensor = frame_tensor.float() / 255.0  # Normalize pixel values to [0, 1]
                frame_tensor = frame_tensor.unsqueeze(0)  # Add batch dimension

                # Run YOLOv8 inference on the frame
                results = pose_model.model(frame_tensor)

                # Visualize the results on the frame
                annotated_frame = results[0].plot()

                # Display the annotated frame
                cv2.imshow("YOLOv8 Inference", annotated_frame)

                # Extract keypoints from YOLOv8 results
                keypoints = self.extract_keypoints(results)

                # Add keypoints to data dictionary
                self.add_keypoints_to_data(keypoints, data)

                # Break the loop if 'q' is pressed
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            else:
                # Break the loop if the end of the video is reached
                break

 

        # Calculate gait data
        data['total_frames'] = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        data['fps'] = cap.get(cv2.CAP_PROP_FPS)
        data['right_gait_duration'], data['right_gait_start'] = self._calculate_period_phase(data['right_ankle'])
        data['left_gait_duration'], data['left_gait_start'] = self._calculate_period_phase(data['left_ankle'])

        # Release the video capture object and close the display window
        cap.release()
        cv2.destroyAllWindows()       
        print('THIS IS THE DATA--------------', data)
        return data

    def _detect_person(self):
        """
        Determines whether there is one person in the image or video.
        :return: True if there is one person in the image or video, False otherwise.
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
    def _calculate_period_phase(coordinates):
        """
        Calculates the duration of a gait and the start of one complete gait.
        Models y coordinates of ankle to sine function.
        :param coordinates: List of coordinates of ankle.
        :return: Dictionary containing duration of gait (period) and start of one complete gait (phase).
        """
        times = np.array(range(0, len(coordinates), 1))
        y_coordinates = np.array([coord[1] for coord in coordinates])
        if len(times) == 0:
            return 0, 0
        ff = np.fft.fftfreq(len(times), 1)
        Fyy = np.abs(np.fft.fft(y_coordinates))
        guess_frequency = np.abs(ff[np.argmax(Fyy[1:]) + 1])
        guess_amplitude = np.std(y_coordinates) * 2.0 ** 0.5
        guess_offset = np.mean(y_coordinates)
        guess = np.array([guess_amplitude, 2.0 * np.pi * guess_frequency, 0.0, guess_offset])

        def sine_function(t, A, w, p, c): return A * np.sin(w * t + p) + c

        popt, _ = scipy.optimize.curve_fit(sine_function, times, y_coordinates, p0=guess)
        A, w, p, _ = popt
        f = w / (2.0 * np.pi)
        T = 1.0 / f
        return T, p

    @staticmethod
    def extract_keypoints(results):
        """
        Extracts keypoints from YOLOv8 results.
        :param results: YOLOv8 results.
        :return: List of keypoints.
        """
        if hasattr(results[0], 'keypoints'):
            return results[0].keypoints.xyn.cpu().numpy()[0]
        else:
            return None

    @staticmethod
    def add_keypoints_to_data(keypoints, data):
        """
        Adds keypoints to data dictionary.
        :param keypoints: List of keypoints.
        :param data: Data dictionary.
        """
        if keypoints is not None:
            data['right_shoulder'].append(keypoints[6])
            data['right_elbow'].append(keypoints[8])
            data['right_wrist'].append(keypoints[10])
            data['left_shoulder'].append(keypoints[5])
            data['left_elbow'].append(keypoints[7])
            data['left_wrist'].append(keypoints[9])
            data['right_hip'].append(keypoints[12])
            data['right_knee'].append
