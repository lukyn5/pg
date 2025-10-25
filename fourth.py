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
    # dvojí krok ze startovní pozice (řada 1)
    if x == 1 and tx == x + 2:
        # pole přes které přechází (x+1, y) musí být volné
        if (x + 1, y) in obsazene_pozice:
            return False
        return True
    return False 


def je_tah_mozny_vez(vez, cilova_pozice, obsazene_pozice):
    x, y = vez["pozice"]   # x = řádek, y = sloupec
    tx, ty = tuple(cilova_pozice)

    if (tx, ty) in obsazene_pozice:
        return False

    if (((ty - y) == 0) and (abs(tx - x) > 0)):
        if tx > x:
            for i in range(x + 1, tx):
                if (i, ty) in obsazene_pozice:
                    return False


        if x > tx:
            for i in range(tx + 1, x):
                if (i, ty) in obsazene_pozice:
                    return False
        return True
    
    
    elif (((tx - x) == 0) and (abs(ty - y) > 0)):
        if ty > y:
            for i in range(y + 1, ty):
                if (tx, i) in obsazene_pozice:
                    return False

        if y > ty:
            for i in range(ty + 1, y):
                if (tx, i) in obsazene_pozice:
                    return False

        return True
    else:
        return False


def je_tah_mozny_strelec(strelec, cilova_pozice, obsazene_pozice):
    x, y = strelec["pozice"]   # x = řádek, y = sloupec
    tx, ty = cilova_pozice
    dx = tx - x
    dy = ty - y


    if ((abs(dx) == 0) or (abs(dy) == 0)):
        return False
    # Střelec se musí pohybovat diagonálně
    if abs(dx) != abs(dy):
        return False

    # Určíme krok pro iteraci po diagonále
    krok_x = 1 if dx > 0 else -1
    krok_y = 1 if dy > 0 else -1

    # Projdeme všechna políčka mezi startem a cílem
    for i in range(1, abs(dx)):
        mezilehla_pozice = (x + i * krok_x, y + i * krok_y)
        if mezilehla_pozice in obsazene_pozice:
            return False

    # Cílové pole může být volné
    if cilova_pozice in obsazene_pozice:
        return False

    return True



def je_tah_mozny_dama(dama, cilova_pozice, obsazene_pozice):
    x, y = dama["pozice"]   # x = řádek, y = sloupec

    return je_tah_mozny_vez(dama, cilova_pozice, obsazene_pozice) or je_tah_mozny_strelec(dama, cilova_pozice, obsazene_pozice)
    

def je_tah_mozny_jezdec(jezdec, cilova_pozice, obsazene_pozice):
    x, y = jezdec["pozice"]   # x = řádek, y = sloupec
    tx, ty = tuple(cilova_pozice)
    
    if abs(ty - y) >= 3:
        return False

    if abs(tx - x) >= 3:
        return False

    if (tx, ty) in obsazene_pozice:
        return False
    if (abs(ty - y) + abs(tx - x)) != 3:
        return False
    return True

def je_tah_mozny_kral(kral, cilova_pozice, obsazene_pozice):
    x, y = kral["pozice"]   # x = řádek, y = sloupec
    tx, ty = tuple(cilova_pozice)

    dx = abs(tx - x)
    dy = abs(ty - y)
    
    # Král se může pohnout jen o jedno pole ve všech směrech
    if dx <= 1 and dy <= 1 and (dx != 0 or dy != 0):
        # Cílové pole nesmí být obsazeno (pro zjednodušení)
        if cilova_pozice in obsazene_pozice:
             if cilova_pozice != kral["pozice"]:
                return False
        return True
        
    return False
    

    pass




def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    x, y = tuple(cilova_pozice)

    if 0 < x < 9 and 0 < y < 9:
        #Daná pozice je na šachovnici
        pass
        
    else:
        #Daná pozice je mimo šachovnici
        return False

    if figurka == pesec:
        return je_tah_mozny_pesak(figurka, cilova_pozice, obsazene_pozice)
    
    if figurka == vez:
        return je_tah_mozny_vez(figurka, cilova_pozice, obsazene_pozice)
    
    if figurka == strelec:
        return je_tah_mozny_strelec(figurka, cilova_pozice, obsazene_pozice)
    
    if figurka == dama:
        return je_tah_mozny_dama(figurka, cilova_pozice, obsazene_pozice)
    
    if figurka == jezdec:
        return je_tah_mozny_jezdec(figurka, cilova_pozice, obsazene_pozice)
    
    if figurka == kral:
        return je_tah_mozny_kral(figurka, cilova_pozice, obsazene_pozice)


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
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o dvě pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True