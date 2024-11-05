from Jarat import Jarat


class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar, idopont, fapados):
        super().__init__(jaratszam, celallomas, jegyar, idopont)
        self._fapados = True

        self._fapados = fapados

    @property
    def fapados(self):
        return self._fapados

    @fapados.setter
    def fapados(self, fapados):
        self._fapados = fapados

    def __str__(self):
        kiiras = "Fapados" if self._fapados else "Nem fapados"

        return super().__str__() + f"{kiiras}"
