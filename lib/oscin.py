try:
    import pythonosc
    from pythonosc.dispatcher import Dispatcher
    from pythonosc.osc_server import BlockingOSCUDPServer
except ImportError:
	print("pythonosc library was not found. Please install it via `pip3 install python-osc` and try again.")
	import sys
	sys.exit(1)

from settings import *

class OscIn:
    def __init__(self, _ip, _port):
        self.ip, self.port = _ip, _port
        self.currentTimePlayer1, self.totalTimePlayer1 = 0.0, 0.0
        self.currentTimePlayer2, self.totalTimePlayer2 = 0.0, 0.0
        self.filePlayer1, self.filePlayer2 = 'no-media', 'no-media'
        self.pausedPlayer1, self.pausedPlayer2 = False, False
        self.loopPlayer1, self.loopPlayer2 = False, False

    def connecta_osc(self):
        self.disp = Dispatcher()
        self.disp.map(OSC_TIME_ROUTES[0], self.getTimeFromOscPlayer1)
        self.disp.map(OSC_TIME_ROUTES[1], self.getTimeFromOscPlayer2)
        self.disp.map(OSC_FILE_NAMES[0], self.getFileFromOscPlayer1)
        self.disp.map(OSC_FILE_NAMES[1], self.getFileFromOscPlayer2)
        self.disp.map(OSC_LAYER_PAUSED[0], self.getPauseFromOscPlayer1)
        self.disp.map(OSC_LAYER_PAUSED[1], self.getPauseFromOscPlayer2)
        self.disp.map(OSC_LAYER_LOOP[0], self.getLoopFromOscPlayer1)
        self.disp.map(OSC_LAYER_LOOP[1], self.getLoopFromOscPlayer2)
        self.srv = BlockingOSCUDPServer( (self.ip, self.port), self.disp)

    def inicia_osc(self):
        self.srv.serve_forever()

    def getTimeFromOscPlayer1(self, addr, currPlayer1, totalPlayer1):
        self.currentTimePlayer1 = currPlayer1
        self.totalTimePlayer1 = totalPlayer1

    def getTimeFromOscPlayer2(self, addr, currPlayer2, totalPlayer2):
        self.currentTimePlayer2 = currPlayer2
        self.totalTimePlayer2 = totalPlayer2

    def getFileFromOscPlayer1(self, addr, path):
        self.filePlayer1 = path

    def getFileFromOscPlayer2(self, addr, path):
        self.filePlayer2 = path

    def getPauseFromOscPlayer1(self, addr, paused):
        self.pausedPlayer1 = paused

    def getPauseFromOscPlayer2(self, addr, paused):
        self.pausedPlayer2 = paused

    def getLoopFromOscPlayer1(self, addr, loop):
        self.loopPlayer1 = loop

    def getLoopFromOscPlayer2(self, addr, loop):
        self.loopPlayer2 = loop