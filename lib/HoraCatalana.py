from datetime import datetime


class HoraCatalana:
    """
    Mòdul que retorna l'hora en català en sistema de campanar.

    ...

    Attributes
    ----------
    >>> horacat : str
        String que conté la hora escrita en català

    Methods
    -------
    >>> tic()
        Actualitza la hora a l'actual

    >>> frase(h, m)
        Retorna la hora en català amb els valors d'hora i minuts personalitzats
    """

    def __init__(self, dt=None):
        """
        Parameters
        ----------
        >>> dt : datetime
            (Opcional) Inicialitzar HoraCatalana amb un objecte datetime.
            Si no consta, s'inicialitzarà amb l'hora actual.

            Exemple:
            >>> from datetime import time
            >>> HoraCatalana( time(12,34) )
        """
        # Atributs públics
        self.horacat = None

        # Atributs privats
        self.__dt = dt if dt else None

        # Variables / Look-up tables
        self.dictHora = {
            0: 'dotze',
            1: 'una',
            2: 'dues',
            3: 'tres',
            4: 'quatre',
            5: 'cinc',
            6: 'sis',
            7: 'set',
            8: 'vuit',
            9: 'nou',
            10: 'deu',
            11: 'onze'
        }

        self.dictMin = {
            1: 'un',
            2: 'dos',
            3: 'tres',
            4: 'quatre',
            5: 'cinc',
            6: 'sis',
            7: 'set',
            8: 'vuit',
            9: 'nou',
        }

        self.rangPrefixMinutsPlural = [
            0, 1, 2, 3, 4, 5, 6, 8, 9, 53, 54, 55, 56, 57, 58, 59]

        # Inicialitza
        self.tic() if not dt else self.__updateFrase()

    # ------------------ #
    # Mètodes públics    #
    # ------------------ #
    def tic(self):
        self.__dt = datetime.now()
        self.__updateFrase()

    def frase(self, h, m):
        if m not in range(0, 60):
            raise Exception("Minut fora del rang 00-59")

        txt = None
        prefix = None

        h += 1
        hora = self.__prefixHora(h)['horaText']

        if m in self.rangPrefixMinutsPlural:
            prefix = self.__prefixHora(h)['prefix2']
        else:
            prefix = self.__prefixHora(h)['prefix1']

        # A __:00 :
        # 01:00 --> És la una en punt
        # 14:00 --> Són les dues en punt
        if m == 0:
            h -= 1
            hora = self.__prefixHora(h)['horaText']
            prefix = self.__prefixHora(h)['prefix2']

            txt = "{0} {1}{2} en punt".format(
                self.__pluralSon(h), prefix, hora)

        # DE __:01 A __:06 I __:08 A __:09 :
        # 01:01 --> És la una i un minut
        # 14:02 --> Són les dues i dos minuts
        elif m in [1, 2, 3, 4, 5, 6, 8, 9]:
            h -= 1
            hora = self.__prefixHora(h)['horaText']
            prefix = self.__prefixHora(h)['prefix2']

            txt = "{0} {1}{2} i {3} {4}".format(
                self.__pluralSon(h),
                prefix,
                hora,
                self.dictMin[m],
                self.__pluralMin(m)
            )

        # A __:07 :
        # 13:07 --> És mig quart de dues
        # 02:07 --> És mig quart de tres
        elif m == 7:
            txt = "És mig quart {0}{1}".format(prefix, hora)

        # DE __:10 A __:14 :
        # 12:10 --> Falten cinc minuts per un quart d'una
        # 00:14 --> Falta un minut per un quart d'una
        elif m in range(10, 15):
            txt = self.__stringPreviQuart(m, 15, prefix, hora)

        # DE __:23 A __:29 :
        # 00:23 --> Falten set minuts per dos quarts d'una
        # 12:29 --> Falta un minut per dos quarts d'una
        elif m in range(23, 30):
            txt = self.__stringPreviQuart(m, 30, prefix, hora)

        # DE __:38 A __:44 :
        # 00:38 --> Falten set minuts per tres quarts d'una
        # 12:44 --> Falta un minut per tres quarts d'una
        elif m in range(38, 45):
            txt = self.__stringPreviQuart(m, 45, prefix, hora)

        # A __:15, __:30 I __:45 :
        # 00:15 --> És un quart d'una
        # 00:30 --> Són dos quarts d'una
        # 00:45 --> Són tres quarts d'una
        elif m in [15, 30, 45]:
            txt = "{0} {1} {2} {3}{4}".format(
                'És' if m == 15 else 'Són',
                self.__quart(m)['prefix'],
                self.__quart(m)['q'],
                prefix,
                hora
            )

        # A __:22, __:37 I __:52 :
        # 12:22 --> És un quart i mig d'una
        # 12:37 --> Són dos quarts i mig d'una
        # 12:52 --> Són tres quarts i mig d'una
        elif m in [22, 37, 52]:
            txt = "{0} {1} {2} i mig {3}{4}".format(
                'És' if m == 22 else 'Són',
                self.__quart(m-7)['prefix'],
                self.__quart(m-7)['q'],
                prefix,
                hora
            )

        # DE __:16 A __:21
        # 13:16 --> És un quart i u de dues
        # 02:21 --> És un quart i sis de tres
        elif m in range(16, 22):
            txt = self.__stringPostQuart(m, 15, prefix, hora)

        # DE __:31 A __:36
        # 01:31 --> Són dos quarts i u de dues
        # 14:36 --> Són dos quarts i sis de tres
        elif m in range(31, 37):
            txt = self.__stringPostQuart(m, 30, prefix, hora)

        # DE __:46 A __:51
        # 01:46 --> Són tres quarts i u de dues
        # 14:51 --> Són tres quarts i sis de tres
        elif m in range(46, 52):
            txt = self.__stringPostQuart(m, 45, prefix, hora)

        # DE __:53 A __:59
        # 12:53 --> Falten set minuts per la una
        # 01:59 --> Falta un minut per les dues
        elif m in range(53, 60):
            txt = "{0} {1} {2} per {3}{4}".format(
                self.__pluralFalta(60-m),
                self.dictMin[60-m],
                self.__pluralMin(60-m),
                prefix,
                hora
            )

        else:
            txt = "ERROR"

        return txt

    # ------------------ #
    # Mètodes privats    #
    # ------------------ #
    def __str__(self):
        return self.horacat

    __repr__ = __str__

    def __updateFrase(self):
        self.horacat = self.frase(
            h=int("{0:%H}".format(self.__dt)),
            m=int("{0:%M}".format(self.__dt))
        )

    def __prefixHora(self, _h):
        h = _h % 12

        prefixos = {
            'prefix1': None,
            'prefix2': None,
            'horaText': self.dictHora[h]
        }

        if h == 1:
            prefixos['prefix1'] = "d'"
            prefixos['prefix2'] = "la "
        elif h == 11:
            prefixos['prefix1'] = "d'"
            prefixos['prefix2'] = "les "
        else:
            prefixos['prefix1'] = "de "
            prefixos['prefix2'] = "les "

        return prefixos

    def __pluralMin(self, m):
        return 'minut' if m == 1 else 'minuts'

    def __pluralFalta(self, m):
        return 'Falta' if m == 1 else 'Falten'

    def __pluralSon(self, h):
        return 'És' if (h == 1) or (h == 13) else 'Són'

    def __quart(self, m):
        if m not in [15, 30, 45]:
            raise Exception("Minuts no vàlids, no són 15, 30 ni 45")

        ret = {'prefix': None, 'q': None}
        if m == 15:
            ret['prefix'] = "un"
            ret['q'] = "quart"
        if m == 30:
            ret['prefix'] = "dos"
            ret['q'] = "quarts"
        if m == 45:
            ret['prefix'] = "tres"
            ret['q'] = "quarts"

        return ret

    def __stringPreviQuart(self, m, properQuart, prefix, hora):
        txt = "{0} {1} {2} per {3} {4} {5}{6}".format(
            self.__pluralFalta(properQuart-m),
            self.dictMin[properQuart-m],
            self.__pluralMin(properQuart-m),
            self.__quart(properQuart)['prefix'],
            self.__quart(properQuart)['q'],
            prefix,
            hora
        )
        return txt

    def __stringPostQuart(self, m, quartPassat, prefix, hora):
        txt = "{0} {1} {2} i {3} {4}{5}".format(
            'És' if quartPassat == 15 else 'Són',
            self.__quart(quartPassat)['prefix'],
            self.__quart(quartPassat)['q'],
            self.dictMin[m-quartPassat] if (m-quartPassat) != 1 else 'u',
            prefix,
            hora
        )
        return txt


# ------------------ #
# Test               #
# ------------------ #
if __name__ == "__main__":
    from datetime import time

    hc = HoraCatalana()
    textdump = ""
    for _h in range(0, 24):
        for _m in range(0, 60):
            text = "{0:02d}:{1:02d} --> {2}".format(_h, _m, hc.frase(_h, _m))
            textdump += text+'\n'
            print(text)

    with open('textdump.txt', 'w', encoding='utf-8') as fd:
        fd.write(textdump)

    print("")
    hc1 = HoraCatalana(time(12, 34))
    print("12:34 --> Són dos quarts i quatre d'una?")
    print("{0:%H:%M} --> {1}".format(time(12,34), hc1))
    hc1.tic()
    print("")
    print("Hora actual:")
    print("{0:%H:%M} --> {1}".format(datetime.now(), hc1))
    # print(hc1)
