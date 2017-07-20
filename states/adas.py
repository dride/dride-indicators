#Need neopixel

import time

from neopixel import *


class Adas(object):

        def __init__(self, stick):

                self.stick = stick
                self.start()

        # Define functions which animate LEDs in various ways.
        def colorWipe(self, color, wait_ms=50):
                """Wipe color across display a pixel at a time."""
                for i in range(self.stick.numPixels()):
                        self.stick.setPixelColor(i, color)
                        self.stick.show()
                        time.sleep(wait_ms/1000.0)

        def theaterChase(self, color, wait_ms=50, iterations=10):
                """Movie theater light style chaser animation."""
                for j in range(iterations):
                        for q in range(3):
                                for i in range(0, self.stick.numPixels(), 3):
                                        self.stick.setPixelColor(i+q, color)
                                self.stick.show()
                                time.sleep(wait_ms/1000.0)
                                for i in range(0, self.stick.numPixels(), 3):
                                        self.stick.setPixelColor(i+q, 0)


        def rainbowCycle(self, wait_ms=20, iterations=5):
                """Draw rainbow that uniformly distributes itself across all pixels."""
                for j in range(256*iterations):
                        for i in range(self.stick.numPixels()):
                                self.stick.setPixelColor(i, self.wheel((int(i * 256 / self.stick.numPixels()) + j) & 255))
                        self.stick.show()
                        time.sleep(wait_ms/1000.0)

        def wheel(self, pos):
                """Generate rainbow colors across 0-255 positions."""
                if pos < 85:
                        return Color(pos * 3, 255 - pos * 3, 0)
                elif pos < 170:
                        pos -= 85
                        return Color(255 - pos * 3, 0, pos * 3)
                else:
                        pos -= 170
                        return Color(0, pos * 3, 255 - pos * 3)

        def dimColor (self, color):
                """ Color is an 32-bit int that merges the values into one """
                return (((color&0xff0000)/3)&0xff0000) + (((color&0x00ff00)/3)&0x00ff00) + (((color&0x0000ff)/3)&0x0000ff)

        def start(self):
                count = 0
                while True and count < 2:
                        self.theaterChase(Color(20,   252,   20))  # Red theater chase
                        count +=1

                self.colorWipe(Color(0, 0, 0))  # reset