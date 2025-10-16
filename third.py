def je_prvocislo(cislo):
    if cislo <= 1:
        return False
    
    if cislo == 2:
        return True
    
    for i in range(2, cislo):
        if cislo % i == 0:

            return False
    
    return True


def vrat_prvocisla(maximum):
    result = []

    aktualni = 0

    while aktualni <= maximum:
        if je_prvocislo(aktualni):
            result.append(aktualni)

        aktualni += 1

    return result

if __name__ == "__main__":
    cislo = int(input("Zadej maximum: "))
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)