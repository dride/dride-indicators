from neopixel import *

from adas import Adas
from carAheadRed import CarAhead
from leftLaneDeparture import LeftLaneDeparture
from loading import Loading
from standalone.buttonPress import ButtonPress
from rightLaneDeparture import RightLaneDeparture
from talking import Talking
from wakeWord import WakeWord

from standalone.welcome import Welcome
from standalone.isWaiting import IsWaiting
from standalone.isDownloading import IsDownloading
from standalone.isPaired import IsPaired
from standalone.needToPair import NeedToPair
from standalone.needToLogin import NeedToLogin
from standalone.uploadSuccessfully import UploadSuccessfully
from standalone.done import Done


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
		self.done()
		for i in range(0, self.stick.numPixels()):
			self.stick.setPixelColor(i, Color(0, 0, 0))
			self.stick.show()

	def leftLaneDeparture(self):
		self.colorWipe()
		LeftLaneDeparture(self.stick).start()

	def rightLaneDeparture(self):
		self.colorWipe()
		RightLaneDeparture(self.stick).start()


	def talking(self):
		self.colorWipe()
		Talking(self.stick).start()

	def welcome(self):
		self.colorWipe()
		Welcome(self.stick).start()

	def adas(self):
		self.colorWipe()
		Adas(self.stick).start()


	def wakeWord(self):
		self.colorWipe()
		WakeWord(self.stick).start()


	def carAhead(self):
		self.colorWipe()
		CarAhead(self.stick).start()

	def loading(self):
		self.colorWipe()
		Loading(self.stick).start()


	def buttonPress(self):
		self.colorWipe()
		ButtonPress(self.stick, True).start()

	def buttonPressOffline(self):
		self.colorWipe()
		print "xxx"
		ButtonPress(self.stick, False).start()


	## API controled actions

	def isWaiting(self):
		self.colorWipe()
		IsWaiting(self.stick).start()

	def isDownloading(self):
		self.colorWipe()
		IsDownloading(self.stick).start()

	def needToPair(self):
		self.colorWipe()
		NeedToPair(self.stick).start()

	def isPaired(self):
		self.colorWipe()
		IsPaired(self.stick).start()

	def needToLogin(self):
		self.colorWipe()
		NeedToLogin(self.stick).start()

	def uploadSuccessfully(self):
		self.colorWipe()
		UploadSuccessfully(self.stick).start()

	def done(self):
		Done()