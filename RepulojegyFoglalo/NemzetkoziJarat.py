from Jarat import Jarat


class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar, idopont, van_ebed):
        super().__init__(jaratszam, celallomas, jegyar, idopont)

        self._van_ebed = ""

        self.van_ebed = van_ebed

    @property
    def van_ebed(self):
        return self._van_ebed

    @van_ebed.setter
    def van_ebed(self, value):
        self._van_ebed = value

    def __str__(self):
        kiiras = "Van ebéd" if self._van_ebed else "Nincs ebéd"

        return super().__str__() + f"{kiiras}"
