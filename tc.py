__all__ = ['Tc']
import math

class Tc:
    def __init__(self, _fr, _tc = None):
        self.hh = 0 # SMPTE Hours field
        self.mm = 0 # SMPTE Minutes field
        self.ss = 0 # SMPTE Seconds field
        self.ff = 0 # SMPTE Frames field
        self.fr = _fr # Frame rate
        self.ft = 0 # Total frames equivalent
        self.sec = 0 # Total seconds equivalent

        if _tc is not None:
            if isinstance(_tc, (Tc, str)):
                self.parseFromTc(_tc)
            elif isinstance(_tc, (int, float)):
                self.parseFromSeconds(_tc)


    def __repr__(self):
        return '{0:02d}:{1:02d}:{2:02d}:{3:02d}'.format(self.hh, self.mm, self.ss, self.ff)

    __str__ = __repr__

    def addOneFrame(self):
        hhMax = 99
        mmMax = 59
        ssMax = 59
        ffMax = self.fr - 1

        self.ff += 1
        if (self.ff > ffMax):
            self.ff = 0
            self.ss += 1

            if (self.ss > ssMax):
                self.ss = 0
                self.mm += 1

                if (self.mm > mmMax):
                    self.mm = 0
                    self.hh += 1

                    if (self.hh > hhMax):
                        self.hh = 0
                        self.mm = 0
                        self.ss = 0
                        self.ff = 0

        self.TC2frames()
            
    def TC2frames(self):
        fTotal = 0
        fTotal += self.hh * (self.fr * 60 * 60)
        fTotal += self.mm * (self.fr * 60)
        fTotal += self.ss * (self.fr)
        fTotal += self.ff
        self.ft = fTotal
        return fTotal

    def TC2seconds(self):
        sTotal = 0
        sTotal += self.hh * 60 * 60
        sTotal += self.mm * 60
        sTotal += self.ss
        sTotal += self.ff / self.fr
        self.sec = sTotal
        return sTotal

    def frames2TC(self):
        self.hh = int(self.ft // self.fr // 3600) % 99
        self.mm = int(self.ft // self.fr // 60) % 60
        self.ss = int(self.ft // self.fr) % 60
        self.ff = int(self.ft % self.fr)
        return self

    def parseFromSeconds(self, _sec):
        self.sec = _sec
        self.ft = self.sec * self.fr
        self.frames2TC()

    def parseFromTc(self, _tc):
        tc = _tc
        if isinstance(tc, str):
            try:
                assert len(tc) == 11
            except AssertionError:
                print('Error: Format del TC incorrecte. String no medeix 11.')
                tc = '00:00:00:00'
                
            tc = tc.split(':')

            try:
                assert len(tc) == 4
            except AssertionError:
                print('Error: Format del TC incorrecte. Error en el símbol ":".')
                tc = [00, 00, 00, 00]

            for n in range(4):
                tc[n] = int(tc[n])
                try:
                    assert tc[n] <= [99, 99, 59, self.fr-1][n]
                except AssertionError:
                    print('Error: Format del TC incorrecte. Els números són més grans del esperat. Frame rate: ' + str(self.fr) + ' però he llegit: ' + str(tc[3]))
                    tc[n] = 0
            
            self.hh = tc[0]
            self.mm = tc[1]
            self.ss = tc[2]
            self.ff = tc[3]

            self.TC2frames()
            self.TC2seconds()
            
        elif isinstance(_tc, Tc): # Oju, aquí sobre-escrivim el framerate
            self.hh = _tc.hh
            self.mm = _tc.mm
            self.ss = _tc.ss
            self.ff = _tc.ff
            self.fr = _tc.fr
            self.ft = _tc.ft
            self.sec = _tc.sec
        else:
            print('Error: El TC ha de ser String o del tipus TC')

    def __add__(self, other):
        if self.fr == other.fr:
            tc_ret = Tc(self.fr)
            tc_ret.ft = self.ft + other.ft
            tc_ret.frames2TC()
            return tc_ret
        else:
            print('AVIS: Els Framerates són diferents. Suma pot ser imprecisa. Es retorna un TC a 25fps.')
            print('AVIS: Primer TC: ' + self.__str__() + ' @ ' + str(self.fr))
            print('AVIS: Segon TC : ' + other.__str__() + ' @ ' + str(other.fr))
            tc_ret = Tc(25)
            tc_ret.parseFromSeconds(self.TC2seconds() + other.TC2seconds())
            return tc_ret
    
    def __sub__(self, other):
        if self.fr == other.fr:
            tc_ret = Tc(self.fr)
            tc_ret.ft = abs(other.ft - self.ft)
            tc_ret.frames2TC()
            return tc_ret
        else:
            print('AVIS: Els Framerates són diferents. Resta pot ser imprecisa. Es retorna un TC a 25fps.')
            print('AVIS: Primer TC: ' + self.__str__() + ' @ ' + str(self.fr))
            print('AVIS: Segon TC : ' + other.__str__() + ' @ ' + str(other.fr))
            tc_ret = Tc(25)
            tc_ret.parseFromSeconds(self.TC2seconds() - other.TC2seconds())
            return tc_ret


