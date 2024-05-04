import numpy as np

# Distance between two points
def distance(p1, p2):
    return np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Angle between three points
def angle(p1, p2, p3):
    vec_p1 = p1 - p2
    vec_p3 = p3 - p2
    cosine_angle = np.dot(vec_p1, vec_p3) / (np.linalg.norm(vec_p1) * np.linalg.norm(vec_p3))
    return np.arccos(cosine_angle) * (180.0 / np.pi)


#Returns difference between current arm angle and 90 degrees, the ideal arm angle
#Uses absolute value
def armAngleDifference(shoulder, elbow, wrist):
    return abs(angle(shoulder,elbow,wrist) - 90)

#Returns difference between current arm angle and 180 degrees, the ideal arm angle
#Uses absolute value
def legAngleDifference(hip, knee, ankle):
    #How do we determine which is the back leg? Do we have everyone face one direction?
    return abs(angle(hip, knee, ankle) - 180)


def armAnalytics(keypoints, rightArmAngleDifferences, leftArmAngleDifferences):

    # Right arm has keypoints 6, 8, 10
    rightArmAngleDifferences.append(armAngleDifference(keypoints[6], keypoints[8], keypoints[10]))
    # Left arm has keypoints 5, 7, 9
    leftArmAngleDifferences.append(armAngleDifference(keypoints[5], keypoints[7], keypoints[9]))

#This should only be run when foot hits the ground?
def feetAnalytics(keypoints, strides, backLegDifferences):
    strides.append(distance(keypoints[15], keypoints[16]))

    # if back leg has not hit the ground do not run this?
    #backLegDifferences.append(legAngleDifference(keypoints[]))