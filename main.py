from realtime_service import RealtimeService

from Adafruit_BBIO.SPI import SPI
import Adafruit_BBIO.PWM as PWM

# import Adafruit_BBIO.GPIO as GPIO

from time import sleep


# Constants
RED = "P9_14"
GREEN = "P9_42"
BLUE = "P8_13"


# Globals
leds = SPI(0, 0)
rt = RealtimeService('rt.tntapp.co', 2748)


def init_LEDs():
    PWM.start(RED, 100)         # red
    PWM.start(GREEN, 100)       # green
    PWM.start(BLUE, 100)		# blue


def make_lights_green():
    PWM.set_duty_cycle(RED, 0)
    PWM.set_duty_cycle(GREEN, 100)
    PWM.set_duty_cycle(BLUE, 0)


def make_lights_red():
    PWM.set_duty_cycle(RED, 100)
    PWM.set_duty_cycle(GREEN, 0)
    PWM.set_duty_cycle(BLUE, 0)


def make_lights_blue():
    PWM.set_duty_cycle(RED, 0)
    PWM.set_duty_cycle(GREEN, 0)
    PWM.set_duty_cycle(BLUE, 100)


def turn_on_all_LEDs():
    leds.writebytes([0b00000000])


def turn_off_all_LEDs():
    leds.writebytes([0b11111111])


def flash_n_times(n=int, speed=float):
    for i in range(n):
        turn_on_all_LEDs()
        sleep(speed)
        turn_off_all_LEDs()
        sleep(speed)


def flash_4seconds():
    turn_on_all_LEDs()
    sleep(0.5)
    turn_off_all_LEDs()
    sleep(0.5)
    turn_on_all_LEDs()
    sleep(0.5)
    turn_off_all_LEDs()
    sleep(0.5)
    turn_on_all_LEDs()
    sleep(0.5)
    turn_off_all_LEDs()
    sleep(0.5)
    turn_on_all_LEDs()
    sleep(0.5)
    turn_off_all_LEDs()


# Start execution
init_LEDs()
flash_n_times(n=5, speed=0.3)


@rt.bind('door-1')
def ken_face(data):
    if data['locked'] is True:
        print "led [ OFF    ]"
        make_lights_red()
        turn_on_all_LEDs()
        sleep(5)
    else:
        print "led [     ON ]"
        make_lights_green()
        flash_n_times(n=2, speed=1)

print "Starting doorEndpoint"

while True:
    sleep(1)
