# Need neopixel

import time

from neopixel import *

class WakeWord(object):
	def __init__(self, stick):

		self.stick = stick
		self.start()

	# Define functions which animate LEDs in various ways.
	def colorWipe(self, color, wait_ms=20):
		"""Wipe color across display a pixel at a time."""
		for i in range(self.stick.numPixels()):
			self.stick.setPixelColor(i, color)
			self.stick.show()
			time.sleep(wait_ms / 1000.0)

	def lightOff(self, color, wait_ms=0):
		"""Wipe color across display a pixel at a time."""
		for i in range(self.stick.numPixels()):
			self.stick.setPixelColor(i, color)
			self.stick.show()
			time.sleep(wait_ms / 1000.0)

	def dimColor(self, color):
		""" Color is an 32-bit int that merges the values into one """
		return (((color & 0xff0000) / 3) & 0xff0000) + (((color & 0x00ff00) / 3) & 0x00ff00) + (
		((color & 0x0000ff) / 3) & 0x0000ff)

	def start(self):

		self.colorWipe(Color(255, 255, 255))  # white wipe
		self.colorWipe(Color(0, 0, 0))  # white wipe

		self.colorWipe(Color(255, 255, 255))  # white wipe
		self.colorWipe(Color(0, 0, 0))  # white wipe

		self.colorWipe(Color(255, 255, 255))  # white wipe
		self.colorWipe(Color(0, 0, 0))  # white wipe

