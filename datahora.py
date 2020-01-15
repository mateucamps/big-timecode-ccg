from datetime import datetime

class DataHora:
    def __init__(self):
        self._currentDateTime_ = datetime.now()

        self.diaText = 'Dia'
        self.dia, self.mes, self.any = 0, 0, 0
        self.hora, self.min, self.seg = 0, 0, 0

        self.horaStr = '00:00:00'
        self.dataStr = 'Dia 00/00/0000'

    def updateStrings(self):
        self.horaStr = '{0:02d}:{1:02d}:{2:02d}'.format(self.hora, self.min, self.seg)
        self.dataStr = '{3} {0:02d}/{1:02d}/{2:04d}'.format(self.dia, self.mes, self.any, self.diaText)

    def tick(self):
        self._currentDateTime_ = datetime.now()

        self.any = int('{0:%Y}'.format(self._currentDateTime_))
        self.mes = int('{0:%m}'.format(self._currentDateTime_))
        self.dia = int('{0:%d}'.format(self._currentDateTime_))

        self.diaText = '{0:%A}'.format(self._currentDateTime_)

        self.hora = int('{0:%H}'.format(self._currentDateTime_))
        self.min = int('{0:%M}'.format(self._currentDateTime_))
        self.seg = int('{0:%S}'.format(self._currentDateTime_))

        self.updateStrings()
        #print('DataHora DEBUG: ' + self.horaStr + ' - ' + self.dataStr)