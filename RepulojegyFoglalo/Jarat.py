from abc import ABC, abstractmethod
from datetime import datetime


class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar, idopont):
        self._jaratszam = 0
        self._celallomas = ""
        self._jegyar = 0
        self._idopont = datetime.now()

        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar
        self.idopont = idopont

    @property
    def jaratszam(self):
        return self._jaratszam

    @jaratszam.setter
    def jaratszam(self, jaratszam):
        self._jaratszam = jaratszam

    @property
    def celallomas(self):
        return self._celallomas

    @celallomas.setter
    def celallomas(self, value):
        self._celallomas = value

    @property
    def jegyar(self):
        return self._jegyar

    @jegyar.setter
    def jegyar(self, value):
        if value >= 0:
            self._jegyar = value

    @property
    def idopont(self):
        return self._idopont

    @idopont.setter
    def idopont(self, value):
        ideiglenes_idopont = None

        try:
            ideiglenes_idopont = datetime.strptime(value, '%Y-%m-%d %H:%M')
        except ValueError:
            print(f"Az '{value}' időpont hibás formátumban lett megadva!")

        if ideiglenes_idopont:
            if ideiglenes_idopont > datetime.now():
                self._idopont = ideiglenes_idopont
            else:
                print(f"Visszamenőleg nem lehet időpontot megadni!")

    @abstractmethod
    def __str__(self):
        return f"Járatszám: {self.jaratszam} | Célállomás: {self.celallomas} | Jegyár: {self.jegyar} Ft | Időpont: {self.idopont.date()} {self.idopont.hour}:{self.idopont.minute} | "
