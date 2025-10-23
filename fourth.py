def je_tah_mozny_pesak(pesec, cilova_pozice, obsazene_pozice):
    x, y = pesec["pozice"]   # x = řádek, y = sloupec
    tx, ty = tuple(cilova_pozice)
    # musí být ve stejné sloupci a nesmí být obsazeno cílové pole
    if ty != y:
        return False
    if (tx, ty) in obsazene_pozice:
        return False
    # pohyb jen vpřed
    if tx == x + 1:
        return True
    # dvojí krok ze startovní pozice (řada 2)
    if x == 2 and tx == x + 2:
        # pole přes které přechází (x+1, y) musí být volné
        if (x + 1, y) in obsazene_pozice:
            return False
        return True
    return False 


def je_tah_mozny_vez():
    x, y = vez["pozice"]   # x = řádek, y = sloupec
    tx, ty = tuple(cilova_pozice)
    pass

def je_tah_mozny_strelec():
    pass


def je_tah_mozny_dama():
    if je_tah_mozny_vez() or je_tah_mozny_strelec():
        return True

def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    x, y = tuple(cilova_pozice)

    if 0 < x < 9 and 0 < y < 9:
        print("Daná pozice je na šachovnici")
    else:
        print("Daná pozice je mimo šachovnici")

    if figurka == pesec:
        return je_tah_mozny_pesak(figurka, cilova_pozice, obsazene_pozice)


    




    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    # Implementace pravidel pohybu pro různé figury zde.

    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}






























    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    '''
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o dvě pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True

    


'''