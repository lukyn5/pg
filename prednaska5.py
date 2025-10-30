"""
class ChybaDeleniNulou(Exception):
    pass

def vydel (citatel, jmenovatel):
    if jmenovatel == 0:
        raise ChybaDeleniNulou("Nulou nelze dělit")
    
    return citatel / jmenovatel
    """

import sys

if __name__ == "__main__":
    try:

        name = input("Zadej jmeno souboru k nacteni: ")
        file = open(name, "r")
        data = file.read()
        print(data)
        file.close()
    except FileNotFoundError as e:
        print(f"Soubor {name} nenalezen")

"""
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

    except ChybaDeleniNulou as e:
        print("Pokusili jste se dělit nulou!!!")

    except Exception as e:
        print(f"V nasem programu nastala chyba {e}")
  """

