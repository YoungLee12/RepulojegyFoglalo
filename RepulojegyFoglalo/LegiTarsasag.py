from datetime import datetime

from JegyFoglalas import JegyFoglalas


class Legitarsasag:
    def __init__(self, nev, kod):
        self._nev = ""
        self._kod = ""

        self.nev = nev
        self.kod = kod

        self._jaratok = []
        self._foglalasok = []

    @property
    def nev(self):
        return self._nev

    @nev.setter
    def nev(self, nev):
        self._nev = nev

    @property
    def kod(self):
        return self._kod

    @kod.setter
    def kod(self, kod):
        self._kod = kod

    def jegy_foglalasa(self, celallomas, idopont):
        jarat = self._jarat_keresese(celallomas, idopont)
        if jarat:
            jegyfoglalas = JegyFoglalas(jarat)
            self._foglalasok.append(jegyfoglalas)
            return jegyfoglalas

    def foglalas_lemondasa(self, foglalas_azonosito):
        foglalas = self._foglalas_keresese(foglalas_azonosito)

        if foglalas:
            self._foglalasok.remove(foglalas)

    def foglalasok_listazasa(self):
        for foglalas in self._foglalasok:
            print(foglalas)

    def jarat_hozzaadasa(self, jarat):
        ideiglenes_jaratszam = self.kod + str(jarat.jaratszam)

        if not self._jaratok_tartalmazza(ideiglenes_jaratszam, jarat.celallomas, jarat.idopont):
            jarat.jaratszam = ideiglenes_jaratszam
            self._jaratok.append(jarat)

    def jaratok_listazasa(self):
        for jarat in self._jaratok:
            print(jarat)

    def _jaratok_tartalmazza(self, jaratszam, celallomas, idopont):
        for jarat in self._jaratok:
            if jarat.jaratszam == jaratszam:
                print(f"A járatszámnak egyedinek kell lennie ({jaratszam})!")
                return True
            if jarat.celallomas == celallomas and jarat.idopont == idopont:
                print(f"Két járat nem rendelkezhet ugyanazzal a célállomással, és ugyanazzal az időponttal! ({celallomas}, {idopont})")
                return True

        return False

    def _jarat_keresese(self, celallomas, idopont):
        ellenorzott_idopont = Legitarsasag._idopont_ellenorzese(idopont)

        for jarat in self._jaratok:
            if jarat.celallomas == celallomas and jarat.idopont == ellenorzott_idopont:
                return jarat

        if ellenorzott_idopont:
            print(f"'{celallomas}' célállomáshoz '{idopont}' időponttal nincs rendelve járat rendszerünkben!")

    def _foglalas_keresese(self, foglalas_azonosito):
        for foglalas in self._foglalasok:
            if str(foglalas.azonosito) == foglalas_azonosito:
                return foglalas

        print(f"'{foglalas_azonosito}' azonosítóval nem szerepel foglalás a rendszerünkben!")

    @staticmethod
    def _idopont_ellenorzese(idopont):
        ideiglenes_idopont = None

        try:
            ideiglenes_idopont = datetime.strptime(idopont, '%Y-%m-%d %H:%M')
        except ValueError:
            print(f"Az '{idopont}' időpont hibás formátumban lett megadva!")

        return ideiglenes_idopont
