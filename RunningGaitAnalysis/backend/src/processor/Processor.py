import numpy as np

class Processor(object):

    def __init__(self, video_reader):
        self.data = video_reader.get_data
    
    def arm_analytics():
        """
        calculates average arm angle difference from ideal 90 degrees for right and left arms
        :return: dictionary containing average right and left arm angle difference from 90 degrees
        """
        n = len(data['right_shoulder'])
        right_arm_angle_difference = 0
        right_arm_angle_difference = 0
        for i in range(0, n, 1):
            right_arm_angle_difference += self.__arm_angle_difference(data['right_shoulder'][i], data['right_elbow'][i], data['right_wrist'][i])
            left_arm_angle_difference += self.__arm_angle_difference(data['left_shoulder'][i], data['left_elbow'][i], data['left_wrist'][i])
        right_arm_angle_difference /= n
        left_arm_angle_difference /= n
        return {'right arm angle difference': right_arm_angle_difference, 'left arm angle difference': left_arm_angle_difference}

    def feet_analytics():
        """
        calculates average back leg angle difference from ideal 180 degrees when leg strikes ground
        Returns: average back leg angle difference from 180 degrees when leg strikes ground

        """
        back_leg_difference = 0
        n = 0
        for i in range(0, len(data['right_ankle']), data['right_gait_duration']):
            min_y = float('-inf')
            min_index = i
            for j in range(i, i + data['right_gait_duration'], 1):
                if data['right_ankle'][j][1] < min_y:
                    min_y = data['right_ankle'][j][1]
                    min_index = j
            back_leg_difference += self.__leg_angle_difference(data['right_hip'][min_index], data['right_knee'][min_index], data['right_ankle'][min_index])
            n += 1
        if n == 0:
            return -1
        back_leg_difference /= n
        return back_leg_difference

    def __distance(p1, p2):
        """ Given points, p1 and p2, find the distance between two points
        Args:
            p1, p2 - points given as a np.array corresponding to the
            (x, y)-coordinates
        Returns:
            distance between p1 and p2
        """
        return np.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

    def __angle(p1, p2, p3):
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

    def __arm_angle_difference(shoulder, elbow, wrist):
        """
        Args:
            shoulder, elbow, wrist - points given as a np.array corresponding to
            (x, y)-coordinates
        Returns:
            the absolute difference between current arm angle and 90 degrees,
            the ideal arm angle
        """
        return abs(self.__angle(shoulder, elbow, wrist) - 90)

    def __leg_angle_difference(hip, knee, ankle):
        """
        Args:
            hip, knee, ankle - points given as a np.array corresponding to
            (x, y)-coordinates
        Returns:
            the absolute difference between current leg angle and 180 degrees, the ideal leg angle
        """
        # How do we determine which is the back leg? Do we have everyone face one direction?
        return abs(self.__angle(hip, knee, ankle) - 180)