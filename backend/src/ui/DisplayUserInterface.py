class DisplayUserInterface(object):

    def __init__(self, processor):
        self.processor = processor

    def display_text(self):
        text = ''

        arm_angle_differences = self.processsor.arm_analytics()
        if arm_angle_differences['right arm angle difference'] > 5:
            text += ('Your right arm angle is ' + str(arm_angle_differences['right arm angle difference'])
                     + ' degrees away from the ideal 90 degrees.\n')
        if arm_angle_differences['left arm angle difference'] > 5:
            text += ('Your left arm angle is ' + str(arm_angle_differences['left arm angle difference'])
                     + ' degrees away from the ideal 90 degrees.\n')

        back_leg_angle_difference = self.processor.leg_analytics()
        if back_leg_angle_difference > 5:
            text += ('Your leg angle is ' + str(back_leg_angle_difference)
                     + ' degrees away from the ideal 180 degrees.\n')

        if text == '':
            text += 'Your running gait is healthy.'

        return text
