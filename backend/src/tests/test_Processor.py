import unittest
import os
import sys
import numpy as np

# import from subdirectory in parent directory named processor
script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '..', 'processor')
sys.path.append(mymodule_dir)
import Processor

# import from subdirectory in parent directory named datamanagement
script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '..', 'datamanagement')
sys.path.append(mymodule_dir)
import VideoReader


class TestProcessor(unittest.TestCase):

    def test_distance(self):
        # test 1:
        p1 = np.array([0, 0])
        p2 = np.array([5, 0])
        self.assertAlmostEqual(
            5, Processor.Processor(VideoReader.VideoReader('none'))._distance(p1, p2)
        )

    def test_angle(self):
        # test 1:
        p1 = np.array([0, 0])
        p2 = np.array([5, 0])
        p3 = np.array([5, 5])
        self.assertAlmostEqual(
            90, Processor.Processor(VideoReader.VideoReader('none'))._angle(p1, p2, p3)
        )


if __name__ == '__main__':
    unittest.main()
