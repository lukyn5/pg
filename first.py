def suda_nebo_licha(cislo):
    if cislo % 2 == 0:
        print(f"Číslo {cislo} je sudé")
    else:
        print(f"Číslo {cislo} je liché")
    
if __name__ == "__main__":
    # nadefinovaný vstup
    suda_nebo_licha(5)
    suda_nebo_licha(1000000)
    
    # uživatelský vstup
    vstup = int(input("Zadej číslo: "))
    suda_nebo_licha(vstup)
