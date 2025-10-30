def vydel (citatel, jmenovatel):
    try:
        return citatel / jmenovatel
    except ZeroDivisionError:
        print("Nelze dělit 0")


if __name__ == "__main__":

    try:
        cislo1 = None
        while cislo1 is None:
            try:
                cislo1 = int(input("Zadej čitatel: "))
            except Exception:
                print("Zadej validni cislo")


        cislo2 = int(input("Zadej jmenovatel: "))

        vysledek = vydel(cislo1, cislo2)

        print(vysledek)

    except Exception:
        print("V nasem programu nastala chyba")


