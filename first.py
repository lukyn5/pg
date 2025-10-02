cislo = int(input("Zadej číslo: "))

def suda_nebo_licha(cislo):
    if cislo % 2 == 0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    if suda_nebo_licha(cislo) == True:
        print(f"Číslo {cislo} je sudé")
    else:
        print(f"Číslo {cislo} je liché")