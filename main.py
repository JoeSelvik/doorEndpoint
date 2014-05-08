from realtime_service import RealtimeService

from Adafruit_BBIO.SPI import SPI
import Adafruit_BBIO.PWM as PWM

import Adafruit_BBIO.GPIO as GPIO

from time import sleep


# Constants
RED = "P9_14"
GREEN = "P9_42"
BLUE = "P8_13"

DOORPORT = "P8_10"


# Globals
leds = SPI(0, 0)
rt = RealtimeService('rt.tntapp.co', 2748)


def init_LEDs():
    PWM.start(RED, 100)         # red
    PWM.start(GREEN, 100)       # green
    PWM.start(BLUE, 100)		# blue

    GPIO.setup(DOORPORT, GPIO.OUT)   # LockPort
    GPIO.output(DOORPORT, GPIO.LOW)  # Default low: locked


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


def flash_n_times(n=int, duration=float):
    for i in range(n):
        turn_on_all_LEDs()
        sleep(duration)
        turn_off_all_LEDs()
        sleep(duration)


# Start execution
init_LEDs()
flash_n_times(n=5, duration=0.4)


@rt.bind('door-1')
def ken_face(data):
    if data['locked'] is True:
        print "led [ LOCK    ]"
        make_lights_red()
        GPIO.output(DOORPORT, GPIO.LOW)      # Lock the door
        flash_n_times(n=3, duration=0.2)
        turn_on_all_LEDs()
        sleep(2)
        flash_n_times(n=3, duration=0.2)
    else:
        print "led [     UNLOCK ]"
        make_lights_green()
        turn_on_all_LEDs()
        GPIO.output(DOORPORT, GPIO.HIGH)    # Unlock the door
        sleep(5)
        GPIO.output(DOORPORT, GPIO.LOW)     # Lock the door
        flash_n_times(n=3, duration=0.2)

print "Starting doorEndpoint"

while True:
    sleep(1)
