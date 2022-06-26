from datetime import datetime
from settings import *

class DataHora:
    def __init__(self):
        self._currentDateTime_ = datetime.now() 

        self.diaText = 'Dia'
        self.dia, self.mes, self.any = 0, 0, 0
        self.hora, self.min, self.seg = 0, 0, 0

        self.horaStr = '00:00:00'
        self.dataStr = 'Dia, 00 de mes de 0000'

    def updateStrings(self):
        self.horaStr = '{0:02d}:{1:02d}:{2:02d}'.format(self.hora, self.min, self.seg)
        self.dataStr = '{0}, {1:02d} {2}{4}{3:04d}'.format(self.diaText, self.dia, self.mesText, self.any, " de " if CATALAN_LOCALE else " ")

    def tradueixDia(self, dia):
        angles_catala = {
            'Monday' : 'Dilluns',
            'Tuesday' : 'Dimarts',
            'Wednesday' : 'Dimecres',
            'Thursday' : 'Dijous',
            'Friday' : 'Divendres',
            'Saturday' : 'Dissabte',
            'Sunday' : 'Diumenge'
        }

        dia_cat = None
        try:
            dia_cat = angles_catala[dia]
        except KeyError:
            print("ERROR: Aquest dia no existeix. Està mal escrit?")
        
        return dia_cat

    def tradueixMes(self, mes):
        angles_catala = {
            'January' : 'de gener',
            'February' : 'de febrer',
            'March' : 'de març',
            'April' : 'd\'abril',
            'May' : 'de maig',
            'June' : 'de juny',
            'July' : 'de juliol',
            'August' : 'd\'agost',
            'September' : 'de setembre',
            'October' : 'd\'octubre', 
            'November' : 'de novembre',
            'December' : 'de desembre'
        }

        mes_cat = None
        try:
            mes_cat = angles_catala[mes]
        except KeyError:
            print("ERROR: Aquest mes no existeix. Està mal escrit?")
        
        return mes_cat

    def tick(self):
        self._currentDateTime_ = datetime.now()

        self.any = int('{0:%Y}'.format(self._currentDateTime_))
        self.mes = int('{0:%m}'.format(self._currentDateTime_))
        self.dia = int('{0:%d}'.format(self._currentDateTime_))

        if CATALAN_LOCALE:
            self.diaText = self.tradueixDia('{0:%A}'.format(self._currentDateTime_))
            self.mesText = self.tradueixMes('{0:%B}'.format(self._currentDateTime_))
        else:
            self.diaText = '{0:%A}'.format(self._currentDateTime_)
            self.mesText = '{0:%B}'.format(self._currentDateTime_)


        self.hora = int('{0:%H}'.format(self._currentDateTime_))
        self.min = int('{0:%M}'.format(self._currentDateTime_))
        self.seg = int('{0:%S}'.format(self._currentDateTime_))

        self.updateStrings()

if __name__ == "__main__":
    dh = DataHora()
    dh.tick()
    print(dh.horaStr)
    print(dh.dataStr)
    print(dh.diaText)