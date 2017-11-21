# Need neopixel

import time
import os

from neopixel import *

class IsDownloading(object):
	def __init__(self, stick):
		self.stick = stick

	# Define functions which animate LEDs in various ways.
	def colorWipe(self, color, wait_ms=100):
		""" wipe color across display pixel a time """
		for i in range(self.stick.numPixels()):
			self.stick.setPixelColor(i, color)
			self.stick.show()
			time.sleep(0.05)

		for i in range(self.stick.numPixels()):
			self.stick.setPixelColor(i, Color(0, 0, 0))
			self.stick.show()
			time.sleep(0.05)


	def start(self):
		self.stick.begin()
		f = open(os.path.dirname(__file__) + "/state/isDownloading.txt", 'w')
		f.write("1")
		f.close()
		while True:
			state = open(os.path.dirname(__file__) + "/state/isDownloading.txt", "r").read()
			if (state != "1"):
				return

			self.colorWipe(Color(255, 255, 255))


