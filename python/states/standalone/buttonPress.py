# Need neopixel

import time

from neopixel import *

class ButtonPress(object):

	online = False
	def __init__(self, stick, online):
		self.stick = stick
		self.online = online

	# Define functions which animate LEDs in various ways.
	def colorWipe(self, color, wait_ms=100):
		""" wipe color across display pixel a time """
		for i in range(self.stick.numPixels()):
			self.stick.setPixelColor(i, color)

		self.stick.show()
		time.sleep(1.5)

		for i in range(self.stick.numPixels()):
			self.stick.setPixelColor(i, Color(0, 0, 0))

		self.stick.show()
		time.sleep(0.5)


	def start(self):
		self.stick.begin()
		if self.online:
			self.colorWipe(Color(232, 253, 2))
		else:
			self.colorWipe(Color(0, 255, 0))


