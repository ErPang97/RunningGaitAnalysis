import numpy as np


def distance(p1, p2):
    """ Given points, p1 and p2, find the distance between two points
    Args:
        p1, p2 - points given as a tuple corresponding to the
        (x, y)-coordinates
    Returns:
        distance between p1 and p2
    """
    return np.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def angle(p1, p2, p3):
    """Given three points, p1, p2, p3, calculate the angle formed
    Args:
        p1, p2, p3 - points given as a tuple corresponding to
        (x, y)-coordinates
    Returns:
        angle formed from the line segments formed from p1, p2, p3
    """
    vec_p1 = p1 - p2
    vec_p3 = p3 - p2
    cosine_angle = np.dot(vec_p1, vec_p3) / (np.linalg.norm(vec_p1) * np.linalg.norm(vec_p3))
    return np.arccos(cosine_angle) * (180.0 / np.pi)


def arm_angle_difference(shoulder, elbow, wrist):
    """
    Args:
        shoulder, elbow, wrist - points given as a tuple corresponding to
        (x, y)-coordinates
    Returns:
        the absolute difference between current arm angle and 90 degrees,
        the ideal arm angle
    """
    return abs(angle(shoulder, elbow, wrist) - 90)


def leg_angle_difference(hip, knee, ankle):
    """
    Args:
        hip, knee, ankle - points given as a tuple corresponding to
        (x, y)-coordinates
    Returns:
        the absolute difference between current arm angle and 180 degrees, the ideal arm angle
    """
    # How do we determine which is the back leg? Do we have everyone face one direction?
    return abs(angle(hip, knee, ankle) - 180)


def arm_analytics(keypoints, right_arm_angle_differences, left_arm_angle_differences):
    """
    Args:
        keypoints -
        right_arm_angle_differences -
        left_arm_angle_differences -
    Returns:

    """
    # Right arm has keypoints 6, 8, 10
    right_arm_angle_differences.append(arm_angle_difference(keypoints[6], keypoints[8], keypoints[10]))
    # Left arm has keypoints 5, 7, 9
    left_arm_angle_differences.append(arm_angle_difference(keypoints[5], keypoints[7], keypoints[9]))


# This should only be run when foot hits the ground?
def feet_analytics(keypoints, strides, back_leg_differences):
    """
    Args:
        keypoints -
        strides -
        back_leg_differences -
    Returns:

    """
    strides.append(distance(keypoints[15], keypoints[16]))

    # if back leg has not hit the ground do not run this?
    # back_leg_differences.append(leg_angle_difference(keypoints[]))
