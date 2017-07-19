#Need neopixel

import time
import math

from neopixel import *

LED_COUNT       = 16
LED_PIN         = 10 #12 / 18
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 250     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal


def colorWipe(stick, color, wait_ms=30):
        """ wipe color across display pixel a time """
        speed = 0.05
        stick.setPixelColor(5, color)
        stick.show()
        time.sleep(speed)
        stick.setPixelColor(6, color)
        stick.show()
        stick.setPixelColor(4, color)
        stick.show()
        time.sleep(speed)
        stick.setPixelColor(7, color)
        stick.show()
        stick.setPixelColor(3, color)
        stick.show()
        time.sleep(speed)
        stick.setPixelColor(8, color)
        stick.show()
        stick.setPixelColor(2, color)
        stick.show()
        time.sleep(speed)
        stick.setPixelColor(9, color)
        stick.show()
        stick.setPixelColor(1, color)
        stick.show()
        time.sleep(speed)
        stick.setPixelColor(10, color)
        stick.show()
        stick.setPixelColor(0, color)
        stick.show()
        time.sleep(speed)
        stick.setPixelColor(11, color)
        stick.show()
        stick.setPixelColor(0, color)
        stick.show()
        time.sleep(speed)
        stick.setPixelColor(12, color)
        stick.show()
        stick.setPixelColor(15, color)
        stick.show()
        time.sleep(speed)
        stick.setPixelColor(13, color)
        stick.show()
        stick.setPixelColor(14, color)
        stick.show()

def dimColor (color):
        """ Color is an 32-bit int that merges the values into one """
        return (((color&0xff0000)/3)&0xff0000) + (((color&0x00ff00)/3)&0x00ff00) + (((color&0x0000ff)/3)&0x0000ff)

if __name__ == '__main__':
        # Create neopixel object
        stick = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
        stick.begin()

        print 'Press Ctrl-c to quit.'
        c = 0;

        while(True):
                c = c +1
                colorWipe (stick, Color(255,   255,   255))
                # if c > 10:
                #         break
                time.sleep(0.1)
                colorWipe (stick,Color(0,0,0)) #reset
                time.sleep(0.1)




        # colorWipe (stick,Color(0,0,0)) #reset
