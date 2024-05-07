# OSC CLIENT
# Change this IP to this machine IP address, which
# will receive OSC UDP packets from CCG Server:
OSC_CLIENT_IP = '127.0.0.1'
OSC_CLIENT_PORT = 5253
# You may want to add these lines to your casparcg.conf:
    # <osc>
    #   <predefined-clients>
	#     <predefined-client>
	#       <address> the.ip.written.above  </address>
	#       <port>5253</port>	
	#     </predefined-client>		
	#   </predefined-clients>
	# </osc>

# CASPAR CG SERVER 2.3.0 LTS: Added /foreground/ between layer no. and /file/
# KEEP IN MIND that we can only track one layer per channel.
# (Default: Layer 10)
OSC_TIME_ROUTES = ['/channel/1/stage/layer/10/foreground/file/time',
                   '/channel/2/stage/layer/10/foreground/file/time']

OSC_FILE_NAMES = ['/channel/1/stage/layer/10/foreground/file/name',
                  '/channel/2/stage/layer/10/foreground/file/name']

OSC_LAYER_PAUSED = ['/channel/1/stage/layer/10/foreground/paused',
                    '/channel/2/stage/layer/10/foreground/paused']

OSC_LAYER_LOOP = ['/channel/1/stage/layer/10/foreground/loop',
                  '/channel/2/stage/layer/10/foreground/loop']

# GUI
WINDOW_SIZE = '1280x720'
WINDOW_TITLE = 'big-timecode-ccg'
REFRESH_RATE_MS = 0.03
REMAINING_ORANGE_SEC = 21.0
REMAINING_RED_SEC = 11.0
GUI_FULLSCREEN = False
ALWAYS_ON_TOP = True
HIDE_MOUSE_CURSOR = True

CLOCK_BG_COLOR = 'black'
CLOCK_FG_COLOR = 'red'

HORA_FONT = ('Arial', 120,'bold')
DATA_FONT = ('Arial', 30)
DEFAULT_FONT = ('Arial', 25)
TC_FONT = ('Arial', 35)
REMAINING_TC_FONT = ('Arial', 45)

PLAYER1_TITLE = 'P1'
PLAYER2_TITLE = 'P2'

DISPLAY_FULL_PATH = False

CATALAN_LOCALE = False

SHOW_DATE_YYMMDD = True

"""
## DEFAULTS:
# OSC CLIENT
OSC_CLIENT_IP = '127.0.0.1'
OSC_CLIENT_PORT = 5253

OSC_TIME_ROUTES = ['/channel/1/stage/layer/10/foreground/file/time',
                   '/channel/2/stage/layer/10/foreground/file/time']

OSC_FILE_NAMES = ['/channel/1/stage/layer/10/foreground/file/name',
                  '/channel/2/stage/layer/10/foreground/file/name']

OSC_LAYER_PAUSED = ['/channel/1/stage/layer/foreground/10/paused',
                    '/channel/2/stage/layer/foreground/10/paused']

OSC_LAYER_LOOP = ['/channel/1/stage/layer/10/foreground/loop',
                  '/channel/2/stage/layer/10/foreground/loop']


# GUI
WINDOW_SIZE = '720x576'
WINDOW_TITLE = 'big-timecode-ccg'
REFRESH_RATE_MS = 0.03
REMAINING_ORANGE_SEC = 11.0
REMAINING_RED_SEC = 6.0
GUI_FULLSCREEN = False
ALWAYS_ON_TOP = True
HIDE_MOUSE_CURSOR = True

HORA_FONT = ('Arial', 150,'bold')
DATA_FONT = ('Arial', 30)
DEFAULT_FONT = ('Arial', 25)
TC_FONT = ('Arial', 35)
REMAINING_TC_FONT = ('Arial', 45)

PLAYER1_TITLE = 'Player 1'
PLAYER2_TITLE = 'Player 2'

DISPLAY_FULL_PATH = False

CATALAN_LOCALE = False

SHOW_DATE_YYMMDD = True

"""