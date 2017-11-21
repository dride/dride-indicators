import time
from neopixel import *

from leftLaneDeparture import LeftLaneDeparture
from rightLaneDeparture import RightLaneDeparture
from talking import Talking
from adas import Adas
from wakeWord import WakeWord
from carAheadRed import CarAhead
from loading import Loading
from buttonPress import ButtonPress


class Indicators(object):

	def __init__(self):
		LED_COUNT = 16
		LED_PIN = 10
		LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
		LED_DMA = 5  # DMA channel to use for generating signal (try 5)
		LED_BRIGHTNESS = 120  # Set to 0 for darkest and 255 for brightest
		LED_INVERT = False  # True to invert the signal

		self.stick = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
		self.stick.begin()

	# Define functions which animate LEDs in various ways.
	def colorWipe(self):
		""" wipe color across display pixel a time """

		for i in range(0, self.stick.numPixels()):
			self.stick.setPixelColor(i, Color(0, 0, 0))
			self.stick.show()

	def leftLaneDeparture(self):
		self.leftLaneDeparture = LeftLaneDeparture(self.stick)
		self.colorWipe()


	def rightLaneDeparture(self):
		self.rightLaneDeparture = RightLaneDeparture(self.stick)
		self.colorWipe()


	def talking(self):
		self.talking = Talking(self.stick)
		self.colorWipe()


	def adas(self):
		self.adas = Adas(self.stick)
		self.colorWipe()


	def wakeWord(self):
		self.wake = WakeWord(self.stick)
		self.colorWipe()


	def carAhead(self):
		self.carAhead = CarAhead(self.stick)
		self.colorWipe()

	def loading(self):
		self.loading = Loading(self.stick)
		self.colorWipe()


	def butonPress(self):
		self.buttonPress = ButtonPress(self.stick)
		self.colorWipe()

