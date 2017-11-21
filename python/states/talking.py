# Need neopixel

import time
import math

from neopixel import *

class Talking(object):
	def __init__(self, stick):
		self.stick = stick
		self.start()

	def talking(self, color, wait_ms=30):
		""" wipe color across display pixel a time """
		speed = 0.05
		self.stick.setPixelColor(5, color)
		self.stick.show()
		time.sleep(speed)

		self.stick.setPixelColor(6, color)
		self.stick.show()
		self.stick.setPixelColor(4, color)
		self.stick.show()
		time.sleep(speed)

		self.stick.setPixelColor(7, color)
		self.stick.show()
		self.stick.setPixelColor(3, color)
		self.stick.show()
		time.sleep(speed)
		self.stick.setPixelColor(8, color)
		self.stick.show()
		self.stick.setPixelColor(2, color)
		self.stick.show()
		time.sleep(speed)
		self.stick.setPixelColor(9, color)
		self.stick.show()
		self.stick.setPixelColor(1, color)
		self.stick.show()
		time.sleep(speed)
		self.stick.setPixelColor(10, color)
		self.stick.show()
		self.stick.setPixelColor(0, color)
		self.stick.show()
		time.sleep(speed)
		self.stick.setPixelColor(11, color)
		self.stick.show()
		self.stick.setPixelColor(0, color)
		self.stick.show()
		time.sleep(speed)
		self.stick.setPixelColor(12, color)
		self.stick.show()
		self.stick.setPixelColor(15, color)
		self.stick.show()
		time.sleep(speed)
		self.stick.setPixelColor(13, color)
		self.stick.show()
		self.stick.setPixelColor(14, color)
		self.stick.show()

	def start(self):
		self.stick.begin()
		count = 0

		while True and count < 2:
			count += 1
			self.talking(Color(255, 255, 255))
			# if c > 10:
			#         break
			time.sleep(0.1)
			self.talking(Color(0, 0, 0))  # reset
			time.sleep(0.1)
