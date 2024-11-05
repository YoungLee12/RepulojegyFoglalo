from Jarat import Jarat


class JegyFoglalas:
    _azonosito_szamlalo = 0

    def __init__(self, jarat):
        JegyFoglalas._azonosito_szamlalo += 1
        self._azonosito = self._azonosito_szamlalo
        self._jarat = None

        self.jarat = jarat

    @property
    def azonosito(self):
        return self._azonosito

    @property
    def jarat(self):
        return self._jarat

    @jarat.setter
    def jarat(self, value):
        self._jarat = value

    def __str__(self):
        return f"Foglalás azonosítója: {self._azonosito} | {self._jarat}"
