#Need neopixel

import time

from neopixel import *

LED_COUNT       = 16
LED_PIN         = 12 #12 / 18
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 30     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal


def colorWipe(stick, color, wait_ms=100):
        """ wipe color across display pixel a time """
        for i in range(LED_COUNT):
                stick.setPixelColor(i, color)
                stick.show()
                time.sleep(wait_ms/1000.0)

        for i in range(LED_COUNT):
                stick.setPixelColor(i, Color(0,0,0))
                stick.show()
                time.sleep(wait_ms/1000.0)
 


def dimColor (color):
        """ Color is an 32-bit int that merges the values into one """
        return (((color&0xff0000)/3)&0xff0000) + (((color&0x00ff00)/3)&0x00ff00) + (((color&0x0000ff)/3)&0x0000ff)

if __name__ == '__main__':
        # Create neopixel object
        stick = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
        stick.begin()

        print 'Press Ctrl-c to quit.'

        while(True):
                colorWipe (stick, Color(255,255,255))




        # colorWipe (stick,Color(0,0,0)) #reset
