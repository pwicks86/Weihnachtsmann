import time

numpix = 60

#strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.3, auto_write=False)
strip = {}

def xmas_cycle():
    while True:
        for j in range(2):
            for i in range(60):
                dec = (i / 10) + j
                if dec % 2 == 0:
                    strip[i] = (255,0,0)
                else:
                    strip[i] = (0,255,0)
            #strip.write()
            print(strip)
            time.sleep(1)

import pdb; pdb.set_trace()
xmas_cycle()
