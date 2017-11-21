# Need neopixel

import time

from neopixel import *

class ButtonPress(object):
	def __init__(self):
		LED_COUNT = 16
		LED_PIN = 10
		LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
		LED_DMA = 5  # DMA channel to use for generating signal (try 5)
		LED_BRIGHTNESS = 120  # Set to 0 for darkest and 255 for brightest
		LED_INVERT = False  # True to invert the signal

		self.stick = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
		self.stick.begin()

	def fade(self, r1, g1, b1, w1, r2, g2, b2, w2, steps, interval):
		lastUpdate = time.time() - interval

		for i in range(1, steps + 1):
			r = ((r1 * (steps - i)) + (r2 * i)) / steps
			g = ((g1 * (steps - i)) + (g2 * i)) / steps
			b = ((b1 * (steps - i)) + (b2 * i)) / steps
			w = ((w1 * (steps - i)) + (w2 * i)) / steps

			while ((time.time() - lastUpdate) < interval):
				pass

			print("{: 3d} ({:0.3f}s): {:03d}, {:03d}, {:03d}, {:03d}".format(i, time.time() - lastUpdate, r, g, b, w))
			color = Color(r, g, b, w)
			for j in range(self.stick.numPixels()):
				self.stick.setPixelColor(j, color)
			self.stick.show()

			lastUpdate = time.time()




	# Define functions which animate LEDs in various ways.
	def colorWipe(self, color, wait_ms=100):
		""" wipe color across display pixel a time """

		for i in range(0, 25):
			self.stick.setPixelColor(i, color)
			self.stick.show()


	def start(self):
		self.stick.begin()
		count = 0

		self.fade(0, 0, 0, 255, 255, 255, 0, 0, 0, 2.025)



if __name__ == '__main__':
	ButtonPress().start()