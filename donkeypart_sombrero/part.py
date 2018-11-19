
try:
    from gpiozero import LED
except:
    print('Could not import gpiozero library. This could happen if your computer does not have GPIO pins.')

from donkeypart_PCA9685_actuators import PWMSteering, PWMThrottle, PCA9685


import time


class Sombrero:
    """
    Part for custom donkey hat.
    """

    def __init__(self,
                 steering_channel=0,
                 steering_left_pwm=290,
                 steering_right_pwm=490,
                 throttle_channel=1,
                 throttle_forward_pwm=300,
                 throttle_stopped_pwm=350,
                 throttle_reverse_pwm=490):

        self._setup_board()

        steering_controller = PCA9685(steering_channel)
        self.steering = PWMSteering(controller=steering_controller,
                                    left_pulse=steering_left_pwm,
                                    right_pulse=steering_right_pwm)

        throttle_controller = PCA9685(throttle_channel)
        self.throttle = PWMThrottle(controller=throttle_controller,
                                    max_pulse=throttle_forward_pwm,
                                    zero_pulse=throttle_stopped_pwm,
                                    min_pulse=throttle_reverse_pwm)

        time.sleep(2)

    def _setup_board(self):
        # turn on enable pin so steering and throttle channels work
        self.enable_pin = LED(26, active_high=False)
        self.enable_pin.on()

        # initialize LEDs
        self.led_0 = LED(13, active_high=False)
        self.led_2 = LED(19, active_high=False)

    def run(self, angle, throttle):
        self.steering.run(angle)
        self.throttle.run(throttle)

    def shutdown(self):
        time.sleep(0.1)


if __name__ == "__main__":
    ctl = Sombrero()
    time.sleep(3)

