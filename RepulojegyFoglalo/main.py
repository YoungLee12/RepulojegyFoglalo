from BelfoldiJarat import BelfoldiJarat
from LegiTarsasag import Legitarsasag
from NemzetkoziJarat import NemzetkoziJarat

legitarsasag = Legitarsasag("Malév", "MA")

# A légitársaság kódja a járat hozzáadása után lesz hozzáfűzve
belfoldi_jarat = BelfoldiJarat(1234, "Budapest", 10000, "2024-11-05 13:40", False)
nemzetkozi_jarat1 = NemzetkoziJarat(1235, "Isztambul", 40000, "2024-11-05 13:40", False)
nemzetkozi_jarat2 = NemzetkoziJarat(4567, "Isztambul", 200000, "2024-12-30 23:15", True)

legitarsasag.jarat_hozzaadasa(belfoldi_jarat)
legitarsasag.jarat_hozzaadasa(nemzetkozi_jarat1)
legitarsasag.jarat_hozzaadasa(nemzetkozi_jarat2)

legitarsasag.jegy_foglalasa("Budapest", "2024-11-05 13:40")
legitarsasag.jegy_foglalasa("Isztambul", "2024-12-30 23:15")
legitarsasag.jegy_foglalasa("Isztambul", "2024-12-30 23:15")
legitarsasag.jegy_foglalasa("Budapest", "2024-11-05 13:40")
legitarsasag.jegy_foglalasa("Isztambul", "2024-12-30 23:15")
legitarsasag.jegy_foglalasa("Isztambul", "2024-12-30 23:15")


def felhasznalo_kezelese():
    print("\nÜdvözöljük jegyfoglaló rendszerünkben!")

    while True:
        print(
            "\nVálasszon a megjelenített opciók közül a megfelelő szám beírásával:\n1: Jegyfoglalás\n2: Foglalás lemondása\n3: Foglalások listázása\n4: Kilépés a rendszerből")
        opcio = input()

        match opcio:
            case "1":
                legitarsasag.jaratok_listazasa()

                celallomas = input("Írja be a listából kiválasztott célállomást!\n")
                idopont = input(
                    "Írja be a listából kiválasztott időpontot a megfelelő formátumban! (YYYY-mm-dd HH:MM)\n")

                foglalas = legitarsasag.jegy_foglalasa(celallomas, idopont)

                if foglalas:
                    print(
                        f"Az utazás költsége {foglalas.jarat.jegyar} Forint, Foglalási azonosítója: {foglalas.azonosito}")
                pass
            case "2":
                azonosito = input("Adja meg a foglalás azonosítóját!\n")
                legitarsasag.foglalas_lemondasa(azonosito)
                pass
            case "3":
                print("A foglalások listája:")
                legitarsasag.foglalasok_listazasa()
                pass
            case "4":
                print("Kilépés!")
                return
            case _:
                pass


felhasznalo_kezelese()
