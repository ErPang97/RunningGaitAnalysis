import unittest
import numpy as np


class TestVideoReader(unittest.TestCase, datamanagement.VideoReader):

    def test_detect_person(self):
        # test 1:

        # Load a pre-trained model for Pose Estimation
        model_path = "yolov8n-pose.pt"
        pose_model = PoseEstimation(model_path)

        # Open the image file
        img_path = "../input_videos/run.png"
        data_manager = DataManagement(img_path)

        self.assertTrue(
            data_manager.detect_person(pose_model)
        )

    def test_calculate_period_phase(self):

        # Create coordinates for a sine wave
        x_array = []
        y_array = []
        coordinates = []
        x = np.arange(0, 5 * np.pi, 0.1)
        y = np.sin(x)
        for i in x:
            coordinates.append([x[i], y[i]])

        result = VideoReader.__calculate_period_phase(coordinates)
        self.assertTrue(result.get("period"), 2 * np.pi)
        self.assertTrue(result.get("phase"), 0)


if __name__ == '__main__':
    unittest.main()
