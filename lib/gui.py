from tkinter import *
from tkinter.ttk import Progressbar
from lib.oscin import *
import threading
import time
import lib.tc as tc

from settings import *
from lib.DataHora import DataHora
from lib.filename import getFileFromPath
from lib.HoraCatalana import HoraCatalana

class MainGui:
    def __init__(self, _titol, _mida):
        self.window = Tk()
        self.window.title(_titol)
        self.window.geometry(_mida)
        if HIDE_MOUSE_CURSOR: self.window.config(cursor = "none")
        self.window.attributes('-topmost', ALWAYS_ON_TOP)
        self.window.attributes('-fullscreen', GUI_FULLSCREEN)
        self.window.resizable(True, True)

        self.currTimePlayer1 = 0.0
        self.totalTimePlayer1 = 0.0
        self.restaTimePlayer1 = 0.0

        self.currTimePlayer2 = 0.0
        self.totalTimePlayer2 = 0.0
        self.restaTimePlayer2 = 0.0

        self.currTimeTCPlayer1 = tc.Tc(25)
        self.totalTimeTCPlayer1 = tc.Tc(25)
        self.restaTimeTCPlayer1 = tc.Tc(25)

        self.currTimeTCPlayer2 = tc.Tc(25)
        self.totalTimeTCPlayer2 = tc.Tc(25)
        self.restaTimeTCPlayer2 = tc.Tc(25)

        self.filePlayer1 = 'no-media'
        self.filePlayer2 = 'no-media'

        self.pasuedPlayer1 = False
        self.pasuedPlayer2 = False

        self.dh = DataHora()
        self.hc = HoraCatalana()

        self.font = DEFAULT_FONT
        self.fontTC = TC_FONT
        self.fontTCRestant = REMAINING_TC_FONT
        self.fontHora = HORA_FONT
        self.fontData = DATA_FONT

    def creaGui(self):
        self.zonaHora = Frame(self.window)
        self.zonaPlayers = Frame(self.window)

        self.labelHora = Label(self.zonaHora, text = self.dh.horaStr, font = self.fontHora, bg=CLOCK_BG_COLOR, fg=CLOCK_FG_COLOR)
        if CATALAN_LOCALE:
            self.labelHoraText = Label(self.zonaHora, text = self.hc, font = self.fontData, bg=CLOCK_BG_COLOR, fg=CLOCK_FG_COLOR)
        self.labelData = Label(self.zonaHora, text = self.dh.dataStr, font = self.fontData, bg=CLOCK_BG_COLOR, fg=CLOCK_FG_COLOR)

        self.zonaPlayer1 = Frame(self.zonaPlayers)
        self.zonaPlayer2 = Frame(self.zonaPlayers)

        self.zonaInfoPlayer1 = Frame(self.zonaPlayer1)
        self.zonaInfoEsquerraPlayer1 = Frame(self.zonaInfoPlayer1)
        self.zonaInfoDretaPlayer1 = Frame(self.zonaInfoPlayer1)

        self.labelPlayer1 = Label(self.zonaPlayer1, text = PLAYER1_TITLE, font=self.font, anchor = 'w', bg = 'SkyBlue1')
        self.currTimeLabelPlayer1 = Label(self.zonaInfoEsquerraPlayer1, text='Actual:' if CATALAN_LOCALE else 'Current:', font=self.font, anchor = 'w')
        self.currTimeNumPlayer1 = Label(self.zonaInfoEsquerraPlayer1, text=self.currTimePlayer1, font=self.fontTC)
        self.totalTimeLabelPlayer1 = Label(self.zonaInfoEsquerraPlayer1, text='Total:', font=self.font, anchor = 'w')
        self.totalTimeNumPlayer1 = Label(self.zonaInfoEsquerraPlayer1, text=self.totalTimePlayer1, font=self.fontTC)
        self.restaTimeLabelPlayer1 = Label(self.zonaInfoDretaPlayer1, text='Restant:' if CATALAN_LOCALE else 'Remaining:', font=self.font)
        self.restaTimeNumPlayer1 = Label(self.zonaInfoDretaPlayer1, text=self.restaTimePlayer1, font=self.fontTCRestant, relief='sunken')

        self.progPlayer1 = Progressbar(self.zonaPlayer1, orient='horizontal', mode='determinate')

        self.zonaInfoPlayer2 = Frame(self.zonaPlayer2)
        self.zonaInfoEsquerraPlayer2 = Frame(self.zonaInfoPlayer2)
        self.zonaInfoDretaPlayer2 = Frame(self.zonaInfoPlayer2)

        self.labelPlayer2 = Label(self.zonaPlayer2, text = PLAYER2_TITLE, font=self.font, anchor = 'w', bg = 'SkyBlue4', fg = 'white')
        self.currTimeLabelPlayer2 = Label(self.zonaInfoEsquerraPlayer2, text='Actual:' if CATALAN_LOCALE else 'Current:', font=self.font, anchor = 'w')
        self.currTimeNumPlayer2 = Label(self.zonaInfoEsquerraPlayer2, text=self.currTimePlayer2, font=self.fontTC)
        self.totalTimeLabelPlayer2 = Label(self.zonaInfoEsquerraPlayer2, text='Total:', font=self.font, anchor = 'w')
        self.totalTimeNumPlayer2 = Label(self.zonaInfoEsquerraPlayer2, text=self.totalTimePlayer2, font=self.fontTC)
        self.restaTimeLabelPlayer2 = Label(self.zonaInfoDretaPlayer2, text='Restant:' if CATALAN_LOCALE else 'Remaining:', font=self.font)
        self.restaTimeNumPlayer2 = Label(self.zonaInfoDretaPlayer2, text=self.restaTimePlayer2, font=self.fontTCRestant, relief='sunken')

        self.progPlayer2 = Progressbar(self.zonaPlayer2, orient='horizontal', mode='determinate')

    def posicionaGui(self):
        self.zonaHora.pack(fill = 'x', expand = False)
        self.zonaPlayers.pack(fill = 'both', expand = True)

        self.labelHora.pack(fill = 'x', expand = False)
        if CATALAN_LOCALE:
            self.labelHoraText.pack(fill = 'both', expand = True)
        self.labelData.pack(fill = 'both', expand = True)

        self.zonaPlayer1.pack(fill = 'both', expand = True)
        self.zonaPlayer2.pack(fill = 'both', expand = True)

        self.labelPlayer1.pack(side = 'top', fill = 'both', expand = True)
        self.labelPlayer2.pack(side = 'top', fill = 'both', expand = True)

        self.zonaInfoPlayer1.pack(side = 'top', fill = 'both', expand = True)
        self.zonaInfoEsquerraPlayer1.pack(side = 'left', fill = 'both', expand = True)
        self.zonaInfoDretaPlayer1.pack(side = 'right', fill = 'both', expand = True)

        self.currTimeLabelPlayer1.grid(column = 0, row = 0)
        self.currTimeNumPlayer1.grid(column = 1, row = 0)
        self.totalTimeLabelPlayer1.grid(column = 0, row = 1)
        self.totalTimeNumPlayer1.grid(column = 1, row = 1)

        self.restaTimeLabelPlayer1.pack(side = 'top', fill = 'both', expand = True)
        self.restaTimeNumPlayer1.pack(side = 'top', fill = 'both', expand = True)
        self.progPlayer1.pack(fill = 'both', expand = True, ipady=0)

        self.zonaInfoPlayer2.pack(side = 'top', fill = 'both', expand = True)
        self.zonaInfoEsquerraPlayer2.pack(side = 'left', fill = 'both', expand = True)
        self.zonaInfoDretaPlayer2.pack(side = 'right', fill = 'both', expand = True)

        self.currTimeLabelPlayer2.grid(column = 0, row = 0)
        self.currTimeNumPlayer2.grid(column = 1, row = 0)
        self.totalTimeLabelPlayer2.grid(column = 0, row = 1)
        self.totalTimeNumPlayer2.grid(column = 1, row = 1)

        self.restaTimeLabelPlayer2.pack(side = 'top', fill = 'both', expand = True)
        self.restaTimeNumPlayer2.pack(side = 'top', fill = 'both', expand = True)
        self.progPlayer2.pack(fill = 'both', expand = True, ipady=0)

    def mostraGui(self):
        self.thOsc = threading.Thread(target=self.oscinit, daemon=True)
        self.thOsc.start()
        self.thSleep = threading.Thread(target=self.autoUpdate, daemon=True)
        self.thSleep.start()
        self.window.mainloop()


    def updateTimes(self):
        # Agafem nova Data i Hora
        self.dh.tick()
        self.labelData.config(text = self.dh.dataStr)
        self.labelHora.config(text = self.dh.horaStr)
        if CATALAN_LOCALE:
            self.hc.tic()
            self.labelHoraText.config(text = self.hc)

        # Agafem dades de Caspar-OSC
        self.currTimePlayer1 = self.caspar.currentTimePlayer1
        self.totalTimePlayer1 = self.caspar.totalTimePlayer1
        self.restaTimePlayer1 = self.caspar.totalTimePlayer1 - self.caspar.currentTimePlayer1

        self.currTimePlayer2 = self.caspar.currentTimePlayer2
        self.totalTimePlayer2 = self.caspar.totalTimePlayer2
        self.restaTimePlayer2 = self.caspar.totalTimePlayer2 - self.caspar.currentTimePlayer2

        self.filePlayer1 = self.caspar.filePlayer1
        self.filePlayer2 = self.caspar.filePlayer2

        self.pasuedPlayer1 = self.caspar.pausedPlayer1
        self.pasuedPlayer2 = self.caspar.pausedPlayer2

        # Canviem etiquetes
        self.currTimeTCPlayer1.parseFromSeconds(self.currTimePlayer1)
        self.totalTimeTCPlayer1.parseFromSeconds(self.totalTimePlayer1)
        self.restaTimeTCPlayer1.parseFromSeconds(self.restaTimePlayer1)
        
        self.currTimeNumPlayer1.config(text = self.currTimeTCPlayer1)
        self.totalTimeNumPlayer1.config(text = self.totalTimeTCPlayer1)
        self.restaTimeNumPlayer1.config(text = self.restaTimeTCPlayer1)
        
        self.currTimeTCPlayer2.parseFromSeconds(self.currTimePlayer2)
        self.totalTimeTCPlayer2.parseFromSeconds(self.totalTimePlayer2)
        self.restaTimeTCPlayer2.parseFromSeconds(self.restaTimePlayer2)
        
        self.currTimeNumPlayer2.config(text = self.currTimeTCPlayer2)
        self.totalTimeNumPlayer2.config(text = self.totalTimeTCPlayer2)
        self.restaTimeNumPlayer2.config(text = self.restaTimeTCPlayer2)

        if not DISPLAY_FULL_PATH:
            self.filePlayer1 = getFileFromPath(self.filePlayer1)
            self.filePlayer2 = getFileFromPath(self.filePlayer2)
        
        self.labelPlayer1.config(text = PLAYER1_TITLE + ' ' + ('[▐ ▌] PAUSED' if self.pasuedPlayer1 else '[►] PLAYING') + ': ' + self.filePlayer1)
        self.labelPlayer2.config(text = PLAYER2_TITLE + ' ' + ('[▐ ▌] PAUSED' if self.pasuedPlayer2 else '[►] PLAYING') + ': ' + self.filePlayer2)

        # Modifiquem progressbar i colors
        self.progPlayer1['maximum'] = self.totalTimePlayer1
        self.progPlayer1['value'] = self.currTimePlayer1
        if self.pasuedPlayer1:
            self.restaTimeNumPlayer1.config(bg = 'cyan', fg = 'black')
        else: 
            if self.restaTimePlayer1 < REMAINING_RED_SEC:
                self.restaTimeNumPlayer1.config(bg = 'red', fg = 'white')
            elif self.restaTimePlayer1 < REMAINING_ORANGE_SEC:
                self.restaTimeNumPlayer1.config(bg = 'orange', fg = 'black')
            else:
                self.restaTimeNumPlayer1.config(bg = 'green', fg = 'white')


        self.progPlayer2['maximum'] = self.totalTimePlayer2
        self.progPlayer2['value'] = self.currTimePlayer2
        if self.pasuedPlayer2:
            self.restaTimeNumPlayer2.config(bg = 'cyan', fg = 'black')        
        else:
            if self.restaTimePlayer2 < REMAINING_RED_SEC:
                self.restaTimeNumPlayer2.config(bg = 'red', fg = 'white')
            elif self.restaTimePlayer2 < REMAINING_ORANGE_SEC:
                self.restaTimeNumPlayer2.config(bg = 'orange', fg = 'black')
            else:
                self.restaTimeNumPlayer2.config(bg = 'green', fg = 'white')

    def oscinit(self):
        self.caspar = OscIn(OSC_CLIENT_IP, OSC_CLIENT_PORT)
        self.caspar.connecta_osc()
        self.caspar.inicia_osc()

    def autoUpdate(self):
        while(True):
            self.updateTimes()
            time.sleep(REFRESH_RATE_MS)
