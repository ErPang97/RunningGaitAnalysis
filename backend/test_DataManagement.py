import unittest
from PoseEstimation import *
from DataManagement import *


class TestDataManagement(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
