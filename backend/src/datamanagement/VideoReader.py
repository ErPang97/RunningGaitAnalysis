from ultralytics import YOLO
import numpy, scipy.optimize
import cv2


class VideoReader(object):

    def __init__(self, filename):
        self.filename = filename

    def get_data(self):
        """
        extracts keypoint data from frames of video and calculates gait data
        :return: dictionary containing list of keypoints for right and left shoulder, elbow, wrist, hip, knee, and ankle and right and left gait duration and start
        """
        # Check if there is one person in video
        if not self.detect_person:
            return None

        # Open the video file
        cap = cv2.VideoCapture(filename)

        # Load a pre-trained model for Pose Estimation
        pose_model = YOLO('yolov8n-pose.pt')

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

        # Release the video capture object and close the display window
        cap.release()
        cv2.destroyAllWindows()

    def detect_person(self):
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
