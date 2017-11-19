import board
import random
import neopixel
import time
from touchio import TouchIn
from math import floor
from digitalio import DigitalInOut, Direction, Pull

button = DigitalInOut(board.D0)
button.direction = Direction.INPUT
button.pull = Pull.DOWN

touch2 = TouchIn(board.A2)

numpix = 60
strip = neopixel.NeoPixel(board.D1, numpix, brightness=1, auto_write=False)

def set_all(c):
    for i in range(numpix):
        strip[i] = c

def clear():
    set_all((0,0,0))

def rand_color():
    return tuple(sorted((0, 0xFF, random.randrange(0,255)), key = lambda x: random.random()))

# Xmas colors
class RedGreenMarch():
    def wheel(pos):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if (pos < 0):
            return [0, 0, 0]
        if (pos > 255):
            return [0, 0, 0]
        if (pos < 85):
            return [int(pos * 3), int(255 - (pos*3)), 0]
        elif (pos < 170):
            pos -= 85
            return [int(255 - pos*3), 0, int(pos*3)]
        else:
            pos -= 170
            return [0, int(pos*3), int(255 - pos*3)]
    def run(self, s):
        pass

# Flash and fade
class ColorFlash():
    def __init__(self):
        self.cycles_to_black = 30
        self.cycle_num = 30
        self.color = None
    def run(self):
        if (self.cycle_num >= self.cycles_to_black):
            self.color = rand_color()
            self.cycle_num = 0
        mult = (self.cycles_to_black - self.cycle_num) / self.cycles_to_black
        set_all(tuple([int( mult * x) for x in self.color]))
        strip.write()
        self.cycle_num += 1

# Random every time
class RandomJunk():
    def run(self):
        for i in range(numpix):
            strip[i] = rand_color()
        strip.write()

# Single pixels fall to the end and stack
class Falling():
    def __init__(self):
        clear()
        self.led_pos = 0
        self.end = numpix
        self.color = rand_color()

    def run(self):
        if (self.led_pos >= self.end):
            self.led_pos = 0
            self.end -= 1
        strip[self.led_pos] = self.color
        strip.write()
        if self.led_pos < self.end - 1:
            strip[self.led_pos] = (0,0,0)
        self.led_pos += 1
        if self.end == 0:
            self.led_pos = 0
            self.end = numpix
            self.color = rand_color()

# similar to Falling
class FunFill():
    def __init__(self):
        clear()
        self.i = 0
        self.color = rand_color()

    def run(self):
        strip[self.i] = self.color
        self.i += 1
        if (self.i >= numpix):
            self.i = 0
            self.color = rand_color()

        strip.write()

modes = [FunFill, Falling, RandomJunk, ColorFlash, ]
num_modes = len(modes)
mode_index = 1
active_mode = modes[mode_index]()

last_button = button.value
while True:
    # if (button.value != last_button):
    if touch2.value:
        mode_index = (mode_index + 1) % num_modes
        active_mode = modes[mode_index]()
    active_mode.run()
