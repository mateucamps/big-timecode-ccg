from time import sleep

from lib.gui import *
from settings import *


if __name__ == "__main__":
    sleep(STARTUP_DELAY_SECONDS)
    app = MainGui(WINDOW_TITLE, WINDOW_SIZE)
    app.creaGui()
    app.posicionaGui()
    app.mostraGui()
