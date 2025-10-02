def delitelne_beze_zbytku(cislo):
    if cislo % 3 == 0:
        return True
    else:
        return False



def main():
    vstup = input("zadej číslo: ")
    vstup = int(vstup)
    vstup *= 3
    vstup -= 2

    if vstup > 10:
        print(f"Číslo {vstup} větší než 10")
    elif vstup < 10:
        print(f"Číslo {vstup} je menší než 10")
    else:
        print(f"Číslo {vstup}je to 10")




    otevreny_soubor = open("soubor.txt", "r")
    obsah_souboru = otevreny_soubor.read()
    print(obsah_souboru)


if __name__ == "__main__":

    if delitelne_beze_zbytku(15) == True:
        print("Je dělitelné beze zbytku")
    else:
        print("Není dělitelné beze zbytku")

    main()