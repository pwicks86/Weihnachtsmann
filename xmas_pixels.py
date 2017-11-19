import board
import neopixel
import time
from math import floor

pixpin = board.D1
numpix = 60
strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.3, auto_write=False)

def xmas_cycle():
    while True:
        for j in range(2):
            for i in range(len(strip)):
                dec = (floor(i / 2)) + j
                print(dec)
                if dec % 2 == 0:
                    strip[i] = (255,0,0)
                else:
                    strip[i] = (0,255,0)
            strip.write()
            time.sleep(.1)

xmas_cycle()
