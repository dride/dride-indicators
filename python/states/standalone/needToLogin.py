# Need neopixel

import time

from neopixel import *

class NeedToLogin(object):
	def __init__(self, stick):
		self.stick = stick

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


		self.fade(0, 0, 0, 0, 173, 243, 18, 0, 40, 0.025)
		self.fade(173, 243, 18, 0,  0, 0, 0, 0, 40, 0.025)


