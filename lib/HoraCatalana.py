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

    def __init__(
            self, 
            dt = None, 
            franja = "", 
            prefixFrase = 'son-passen-falten', 
            xarnego = False
            ):
        """
        Parameters
        ----------
        >>> dt : datetime
            (Opcional) Inicialitzar HoraCatalana amb un objecte datetime.
            Si no consta, s'inicialitzarà amb l'hora actual.

            Exemple:
            >>> from datetime import time
            >>> HoraCatalana( time(12,34) )
        
        >>> franja : str
            (Opcional) Mostrar la divisió del dia segons l'època de l'any.
            Possibles valors són 'estiu', 'hivern' o 'auto'.
            Si no s'indica o és un string buit "" no es mostrarà
            la franja horària.

            Exemple:
            >>> HoraCatalana( time(18,45), franja='estiu' ) 
            "Són tres quarts de set de la tarda"
            
            >>> HoraCatalana( time(18,45), franja='hivern' ) 
            "Són tres quarts de set del vespre"

        >>> prefixFrase : str
            (Opcional) Tipus de prefix a l'anunciament de la hora.
            Es pot utilitzar un prefix lliurement, però els especials són:

            (Per defecte) 'son-passen-falten':
                Utilitza els verbs son, passen i falten.
            
            'a':
                Utilitza la preposició A per anunciar una hora futura.

            '': 
                No utilitza cap prefix

            Exemple:
            >>> HoraCatalana( time(18,45), prefixFrase='son-passen-falten' )
            "Són tres quarts de set de la tarda"
            
            >>> HoraCatalana( time(18,45), prefixFrase='a' )
            "A tres quarts de set de la tarda"

            >>> HoraCatalana( time(18,45), prefixFrase='' )
            "Tres quarts de set de la tarda"

        >>> xarnego : bool
            (Opcional) Mostrar la hora malament

            Exemple:
            >>> HoraCatalana( time(12,30), xarnego=True )   
            Són les dotze i mitja

        """
        # Atributs públics
        self.horacat = None

        # Atributs privats
        self.__dt = dt if dt else None
        self.__franja = franja
        self.__prefixFrase = prefixFrase

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

        self.__xarnego = xarnego
        self.dictHoraXarnego = {
            1: 'la una',
            2: 'les dos',
            3: 'les tres',
            4: 'les quatre',
            5: 'les cinc',
            6: 'les sis',
            7: 'les set', 
            8: 'les vuit',
            9: 'les nou',
            10: 'les deu',
            11: 'les onze',
            00: 'les dotze'
        }

        self.dictMinXarnego = {
            1: 'un',
            2: 'dos',
            3: 'tres',
            4: 'quatre',
            5: 'cinc', 
            6: 'sis', 
            7: 'set',
            8: 'vuit',
            9: 'nou',
            10: 'deu',
            11: 'onze',
            12: 'dotze',
            13: 'tretze',
            14: 'catorze',
            15: 'quart',
            16: 'setze',
            17: 'disset',
            18: 'divuit',
            19: 'dinou',
            20: 'vint',
            21: 'vint-i-un',
            22: 'vint-i-dos',
            23: 'vint-i-tres',
            24: 'vint-i-quatre',
            25: 'vint-i-cinc',
            26: 'vint-i-sis',
            27: 'vint-i-set',
            28: 'vint-i-vuit',
            29: 'vint-i-nou',
            30: 'mitja',
            31: 'trenta-un',
            32: 'trenta-dos',
            33: 'trenta-tres',
            34: 'trenta-quatre',
            35: 'trenta-cinc',
            36: 'trenta-sis',
            37: 'trenta-set',
            38: 'trenta-vuit',
            39: 'trenta-nou',
            40: 'quaranta',
            41: 'quaranta-un',
            42: 'quaranta-dos',
            43: 'quaranta-tres',
            44: 'quaranta-quatre',
            45: 'tres quarts',
            46: 'quaranta-sis',
            47: 'quaranta-set',
            48: 'quaranta-vuit',
            49: 'quaranta-nou',
            50: 'cinquanta',
            51: 'cinquanta-un',
            52: 'cinquanta-dos',
            53: 'cinquanta-tres',
            54: 'cinquanta-quatre',
            55: 'cinquanta-cinc',
            56: 'cinquanta-sis',
            57: 'cinquanta-set',
            58: 'cinquanta-vuit',
            59: 'cinquanta-nou',
            0: 'en punt'
        }

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

        if not self.__xarnego:
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

                if self.__prefixFrase == 'son-passen-falten':
                    prefixFrase = self.__pluralSon(h)
                elif self.__prefixFrase == 'a':
                    prefixFrase = 'A'
                elif self.__prefixFrase == '':
                    prefixFrase = ''
                else:
                    prefixFrase = self.__prefixFrase
                

                txt = "{0} {1}{2} en punt".format(
                    prefixFrase, prefix, hora)

            # DE __:01 A __:06 I __:08 A __:09 :
            # 01:01 --> És la una i un minut
            # 14:02 --> Són les dues i dos minuts
            elif m in [1, 2, 3, 4, 5, 6, 8, 9]:
                h -= 1
                hora = self.__prefixHora(h)['horaText']
                prefix = self.__prefixHora(h)['prefix2']

                if self.__prefixFrase == 'son-passen-falten':
                    prefixFrase = self.__pluralSon(h)
                elif self.__prefixFrase == 'a':
                    prefixFrase = 'A'
                elif self.__prefixFrase == '':
                    prefixFrase = ''
                else:
                    prefixFrase = self.__prefixFrase

                txt = "{0} {1}{2} i {3} {4}".format(
                    prefixFrase,
                    prefix,
                    hora,
                    self.dictMin[m],
                    self.__pluralMin(m)
                )

            # A __:07 :
            # 13:07 --> És mig quart de dues
            # 02:07 --> És mig quart de tres
            elif m == 7:

                if self.__prefixFrase == 'son-passen-falten':
                    prefixFrase = "És"
                elif self.__prefixFrase == 'a':
                    prefixFrase = 'A'
                elif self.__prefixFrase == '':
                    prefixFrase = ''
                else:
                    prefixFrase = self.__prefixFrase

                txt = "{0} mig quart {1}{2}".format(prefixFrase, prefix, hora)

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

                if self.__prefixFrase == 'son-passen-falten':
                    prefixFrase = 'És' if m == 15 else 'Són'
                elif self.__prefixFrase == 'a':
                    prefixFrase = 'A'
                elif self.__prefixFrase == '':
                    prefixFrase = ''
                else:
                    prefixFrase = self.__prefixFrase

                txt = "{0} {1} {2} {3}{4}".format(
                    prefixFrase,
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

                if self.__prefixFrase == 'son-passen-falten':
                    prefixFrase = 'És' if m == 22 else 'Són'
                elif self.__prefixFrase == 'a':
                    prefixFrase = 'A'
                elif self.__prefixFrase == '':
                    prefixFrase = ''
                else:
                    prefixFrase = self.__prefixFrase

                txt = "{0} {1} {2} i mig {3}{4}".format(
                    prefixFrase,
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

                if self.__prefixFrase == 'son-passen-falten':
                    prefixFrase = self.__pluralFalta(60-m)
                elif self.__prefixFrase == 'a':
                    prefixFrase = 'A'
                elif self.__prefixFrase == '':
                    prefixFrase = ''
                else:
                    prefixFrase = self.__prefixFrase

                txt = "{0} {1} {2} per {3}{4}".format(
                    prefixFrase,
                    self.dictMin[60-m],
                    self.__pluralMin(60-m),
                    prefix,
                    hora
                )

            else:
                txt = "ERROR"


            # Franja horària
            if self.__franja == "":
                pass
            elif self.__franja in ['estiu', 'hivern']:
                txt += " "
                txt += self.__franjaHoraria(h)
            elif self.__franja == 'auto':
                self.__franjaHorariaAuto()
                txt += " "
                txt += self.__franjaHoraria(h)
                pass
            else:
                raise Exception("Franja no vàlida: només pot ser 'estiu', 'hivern' o 'auto'")

            # En cas que no hi hagi prefix, retalla el primer espai
            # i posa la primera lletra en majúscula
            if self.__prefixFrase == '':
                txt = txt[1:].capitalize()

            return txt
        else:
            hora_text = self.dictHoraXarnego.get(h%12)
            min_text = self.dictMinXarnego.get(m)

            plural_minuts = "minut" if m == 1 else "minuts"

            if m == 0:
                return "Són {0} {1}".format(hora_text, min_text)
            elif m in [15, 30, 45]:
                return "Són {0} i {1}".format(hora_text, min_text)
            else:
                return "Són {0} i {1} {2}".format(hora_text, min_text, plural_minuts)

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

        if self.__prefixFrase == 'son-passen-falten':
            prefixFrase = self.__pluralFalta(properQuart-m)
        elif self.__prefixFrase == 'a':
            prefixFrase = 'A'
        elif self.__prefixFrase == '':
            prefixFrase = ''
        else:
            prefixFrase = self.__prefixFrase

        txt = "{0} {1} {2} per {3} {4} {5}{6}".format(
            prefixFrase,
            self.dictMin[properQuart-m],
            self.__pluralMin(properQuart-m),
            self.__quart(properQuart)['prefix'],
            self.__quart(properQuart)['q'],
            prefix,
            hora
        )
        return txt

    def __stringPostQuart(self, m, quartPassat, prefix, hora):

        if self.__prefixFrase == 'son-passen-falten':
            prefixFrase = 'És' if quartPassat == 15 else 'Són'
        elif self.__prefixFrase == 'a':
            prefixFrase = 'A'
        elif self.__prefixFrase == '':
            prefixFrase = ''
        else:
            prefixFrase = self.__prefixFrase

        txt = "{0} {1} {2} i {3} {4}{5}".format(
            prefixFrase,
            self.__quart(quartPassat)['prefix'],
            self.__quart(quartPassat)['q'],
            self.dictMin[m-quartPassat] if (m-quartPassat) != 1 else 'u',
            prefix,
            hora
        )
        return txt

    def __franjaHoraria(self, h):
        # Matinada: 01h a 05h
        if h in range(1, 6):
            return "de la matinada"
        # Matí: 06h a 11h
        elif h in range(6, 12):
            return "del matí"
        # Migdia: 12h a 14h
        elif h in range(12, 15):
            return "del migdia"
        # Tarda-estiu: 15h a 19h
        elif self.__franja == "estiu" and h in range(15, 20):
            return "de la tarda"
        # Tarda-hivern: 15h a 18h
        elif self.__franja == "hivern" and h in range(15, 19):
            return "de la tarda"
        # Vespre-estiu: 20h a 22h
        elif self.__franja == "estiu" and h in range(20, 23):
            return "del vespre"
        # Vespre-hivern: 19h a 22h
        elif self.__franja == "hivern" and h in range(19, 23):
            return "del vespre"
        # Nit: 23h a 00h
        elif h in [23, 24, 00]:
            return "de la nit"
        else:
            return "FRANJA ERROR -- HORA: {}".format(h)

    def __franjaHorariaAuto(self):
        if datetime.now().month in range (4,10):
            self.__franja = 'estiu'
        else:
            self.__franja = 'hivern'



# ------------------ #
# Test               #
# ------------------ #
if __name__ == "__main__":
    from datetime import time

    # TEST 1: Totes les hores de 00:00 a 23:59
    hc = HoraCatalana(franja='auto', prefixFrase='son-passen-falten', xarnego=False)
    textdump = ""
    for _h in range(0, 24):
        for _m in range(0, 60):
            text = "{0:02d}:{1:02d} --> {2}".format(_h, _m, hc.frase(_h, _m))
            textdump += text+'\n'
            print(text)

    with open('textdump.txt', 'w', encoding='utf-8') as fd:
        fd.write(textdump)
    print("")

    # TEST 2: Provem hora 12:34
    hc1 = HoraCatalana(time(12, 34), franja="auto")
    print("12:34 --> Són dos quarts i quatre d'una del migdia?")
    print("{0:%H:%M} --> {1}".format(time(12,34), hc1))
    print("")
    
    # TEST 3: Provem hora actual:
    print("Hora actual:")
    hc1.tic()
    print("{0:%H:%M} --> {1}".format(datetime.now(), hc1))
    
