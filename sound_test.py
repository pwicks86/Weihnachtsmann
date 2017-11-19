import board
import time
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn, AnalogOut
from touchio import TouchIn
import adafruit_dotstar as dotstar

# Analog input on A1
analog1in = AnalogIn(board.A1)

dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)

def getVoltage(pin):
    return (pin.value * 3.3) / 65536

v_max = -500
counter = 0
while True:
  voltage = getVoltage(analog1in) - .67
  voltage = voltage * 10
  mult = voltage / .3
  l = int(255 * mult)
  dot[0] = (l,l,l)
  v_max = max(voltage, v_max)
  counter += 1
  if (counter > 100):
      print(v_max)
      counter = 0
      v_max = -500
  # dot[0] = (255 * ())
  # print("A1: %f" % voltage)
