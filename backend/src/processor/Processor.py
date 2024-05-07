import numpy as np
import math
import os
import sys


class Processor(object):

    def __init__(self, video_reader):
        self.data = video_reader.get_data()

    def arm_analytics(self):
        """
        calculates average arm angle difference from ideal 90 degrees for right and left arms
        :return: 2-tuple, in which first value is average right arm angle difference from 90 degrees and second value is left arm angle difference from 90 degrees
        """
        try:
            print('I am in arm analytics')
            n = len(self.data['right_shoulder'])
            right_arm_angle_difference = 0
            left_arm_angle_difference = 0
            for i in range(n):
                right_arm_angle_difference += Processor._arm_angle_difference(self.data['right_shoulder'][i],
                                                                               self.data['right_elbow'][i],
                                                                               self.data['right_wrist'][i])
                left_arm_angle_difference += Processor._arm_angle_difference(self.data['left_shoulder'][i],
                                                                              self.data['left_elbow'][i],
                                                                              self.data['left_wrist'][i])
            right_arm_angle_difference /= n
            left_arm_angle_difference /= n
            return right_arm_angle_difference, left_arm_angle_difference
        except:
            print(f"Error in arm analytics: {e}")
            return 0, 0


    def feet_analytics(self):
        """
        calculates average back leg angle difference from ideal 180 degrees when leg strikes ground
        Returns: average back leg angle difference from 180 degrees when leg strikes ground, -1 if less than one stride detected
        """
        gait_duration = self.data['right_gait_duration']
        back_leg_difference = 0
        n = 0
        for i in range(0, len(self.data['right_ankle']), gait_duration):
            min_y = float('-inf')
            min_index = i
            for j in range(i, i + gait_duration, 1):
                if self.data['right_ankle'][j][1] < min_y:
                    min_y = self.data['right_ankle'][j][1]
                    min_index = j
            back_leg_difference += Processor._leg_angle_difference(self.data['right_hip'][min_index],
                                                                    self.data['right_knee'][min_index],
                                                                    self.data['right_ankle'][min_index])
            n += 1
        if n == 0:
            return -1
        back_leg_difference /= n
        return back_leg_difference

    def calculate_gait_per_minute(self, data):
        """
        Args:
            data: dictionary of data
        Returns:
            The number of gaits per minute. Each gait is one step
        """
        # Get frames per gait
        right_gait_duration = data['right_gait_duration']
        left_gait_duration = data['left_gait_duration']
        gait_per_frame = 1/(data['total_frames'] / (right_gait_duration + left_gait_duration) * 2)

        return gait_per_frame * data['fps'] * 60

    @staticmethod
    def _distance(p1, p2):
        """ Given points, p1 and p2, find the distance between two points
        Args:
            p1, p2 - points given as a np.array corresponding to the
            (x, y)-coordinates
        Returns:
            distance between p1 and p2
        """
        return np.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

    @staticmethod
    def _angle(p1, p2, p3):
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
    def _arm_angle_difference(shoulder, elbow, wrist):
        """
        Args:
            shoulder, elbow, wrist - points given as a np.array corresponding to
            (x, y)-coordinates
        Returns:
            the absolute difference between current arm angle and 90 degrees,
            the ideal arm angle
        """
        return abs(Processor._angle(shoulder, elbow, wrist) - 90)

    @staticmethod
    def _leg_angle_difference(hip, knee, ankle):
        """
        Args:
            hip, knee, ankle - points given as a np.array corresponding to
            (x, y)-coordinates
        Returns:
            the absolute difference between current leg angle and 180 degrees, the ideal leg angle
        """
        # How do we determine which is the back leg? Do we have everyone face one direction?
        return abs(Processor._angle(hip, knee, ankle) - 180)

