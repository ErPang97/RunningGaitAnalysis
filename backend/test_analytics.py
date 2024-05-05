import unittest
from analytics import *


class TestAnalytics(unittest.TestCase):

    def test_distance(self):
        # test 1:
        p1 = np.array([0, 0])
        p2 = np.array([5, 0])
        self.assertAlmostEqual(
            5, distance(p1, p2)
        )

    def test_angle(self):
        # test 1:
        p1 = np.array([0, 0])
        p2 = np.array([5, 0])
        p3 = np.array([5, 5])
        self.assertAlmostEqual(
            90, angle(p1, p2, p3)
        )

if __name__ == '__main__':
    unittest.main()
