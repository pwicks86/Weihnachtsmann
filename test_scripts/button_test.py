# Gemma IO demo
# Welcome to CircuitPython 2.0.0 :)

import board
import time
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn, AnalogOut
from touchio import TouchIn
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import adafruit_dotstar as dotstar

# dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

button = DigitalInOut(board.D0)
button.direction = Direction.INPUT
button.pull = Pull.DOWN

while True:
  # led.value = button.value
  print(button.value)

