# Need neopixel

import time
import os

from neopixel import *

class Done(object):
	def __init__(self):
		path = os.path.dirname(__file__) + "/state/"
		for filename in os.listdir(path):
			f = open(path + filename, 'w')
			f.write("0")
			f.close()
