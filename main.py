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
    PWM.start(RED, 100)		# red
    PWM.start(GREEN, 100)		# green
    PWM.start(BLUE, 100)		# blue


def turn_on_all_LEDs():
    leds.writebytes([0b00000000])


def turn_off_all_LEDs():
    leds.writebytes([0b11111111])


init_LEDs()


@rt.bind('door-1')
def ken_face(data):
    if data['locked'] is True:
        print "led [ OFF    ]"
        turn_off_all_LEDs()
    else:
        print "led [     ON ]"
        turn_on_all_LEDs()

print "Starting doorEndpoint"

while True:
    sleep(1)
