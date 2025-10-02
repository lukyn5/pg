cislo = int(input("Zadej číslo: "))

def sudy_nebo_lichy(cislo):
    if cislo % 2 == 0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    if sudy_nebo_lichy(cislo) == True:
        print(f"Číslo {cislo} je sudé")
    else:
        print(f"Číslo {cislo} je liché")