import sys
from indicators import Indicators

action = sys.argv[1]

availbleActions = [
					"isWaiting",
					"isDownloading",
					"isPaired",
					"needToPair",
					"needToLogin",
					"uploadSuccessfully",
					"buttonPress",
					"buttonPressOffline",
					"done"

				]

if (action in availbleActions):
	getattr(Indicators(), action)()

