import unittest
import numpy as np
import os
import sys

# import from subdirectory in parent directory named datamanagement
script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '..', 'datamanagement')
sys.path.append(mymodule_dir)
import VideoReader


class TestVideoReader(unittest.TestCase):

    def test_detect_person(self):
        # test 1:

        # Open the image file
        img_path = "../../../input_videos/run.png"
        data_manager = VideoReader.VideoReader(img_path)

        self.assertTrue(
            data_manager._detect_person()
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
