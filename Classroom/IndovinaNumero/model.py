import random

class Model(object):
    def __init__(self):
        self._NMax = 100 # Dobbiamo indovinare un numero tra 1 e 100
        self._Mmax = 6 # Numero massimo di tentativi
        self._Mrim = self._Mmax
        self._segreto = None

    @property
    def NMax(self):
        return self._NMax

    @property
    def Mmax(self):
        return self._Mmax

    @property
    def Mrim(self):
        return self._Mrim

    @property
    def segreto(self):
        return self._segreto

    def inizializza(self):
        self._segreto = random.randint(1, self._NMax)
        self._Mrim = self._Mmax

    def indovina(self, tentativo):
        if self._Mrim == 0:
            return self._Mrim, None
        else:
            self._Mrim -= 1

        if tentativo == self._segreto:
            return self._Mrim, 0

        elif tentativo > self._segreto:
            return self._Mrim, -1

        else:
            return self._Mrim, 1

