from processor.Processor import *


class DisplayData(object):

    def __init__(self, processor):
        self.right_arm_angle_difference, self.left_arm_angle_difference = processor.arm_analytics()
        self.back_leg_difference = processor.feet_analytics
        self.gait_per_minute = processor.calculate_gait_per_minute
