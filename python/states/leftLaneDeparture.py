#Need neopixel

import time

from neopixel import *

class LeftLaneDeparture(object):

	def __init__(self, stick):

		self.stick = stick
		self.start()

	# Define functions which animate LEDs in various ways.
	def colorWipe(self, color, wait_ms=100):
		""" wipe color across display pixel a time """

		for i in range(9, 10):
			self.stick.setPixelColor(i, color)
			self.stick.show()

	def lightOff(self, color, wait_ms=0):
			"""Wipe color across display a pixel at a time."""
			for i in range(self.stick.numPixels()):
				self.stick.setPixelColor(i, color)
				self.stick.show()
				time.sleep(wait_ms/1000.0)

	def dimColor (color):
			""" Color is an 32-bit int that merges the values into one """
			return (((color&0xff0000)/3)&0xff0000) + (((color&0x00ff00)/3)&0x00ff00) + (((color&0x0000ff)/3)&0x0000ff)

	def start(self):
			# Create neopixel object

			count = 0
			while True and count < 4:
				self.colorWipe(Color(252, 249, 50))  # yellow wipe
				time.sleep(0.1)
				self.lightOff(Color(0, 0, 0))  # white wipe
				time.sleep(0.1)
				count += 1

			self.colorWipe(Color(0, 0, 0)) #reset