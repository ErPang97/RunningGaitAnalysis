from PoseEstimation import *
import cv2

if __name__ == "__main__":

    # load a pre-trained model for Pose Estimation
    model_path = "yolov8n-pose.pt"
    pose_model = PoseEstimation(model_path)

    # Open the video file
    video_path = "../input_videos/mini_run.mp4"
    cap = cv2.VideoCapture(video_path)

    # Initialize arrays
    rightArmAngleDifferences = []
    leftArmAngleDifferences = []
    backLegAngleDifferences = []

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
                print(keypoints_numpy)

                # Add datapoints to arrays
                # Add
            else:
                print("No keypoints attribute found in the results.")

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            # Break the loop if the end of the video is reached
            break

    # Release the video capture object and close the display window
    cap.release()
    cv2.destroyAllWindows()
