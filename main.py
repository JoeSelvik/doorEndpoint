from realtime_service import RealtimeService

from Adafruit_BBIO.SPI import SPI
import Adafruit_BBIO.PWM as PWM

# import Adafruit_BBIO.GPIO as GPIO


# Globals
leds = SPI(0, 0)


def init_LEDs():
    PWM.start("P9_14", 100)		# red
    PWM.start("p9_42", 100)		# green
    PWM.start("P8_13", 100)		# blue


def turn_on_all_LEDs():
    leds.writebytes([0b00000000])


def turn_off_all_LEDs():
    leds.writebytes([0b11111111])


rt = RealtimeService('rt.tntapp.co', 2748)


@rt.bind('door-1')
def ken_face(data):
    if data['locked'] is True:
        print "led [ OFF    ]"
    else:
        print "led [     ON ]"

while True:
    pass