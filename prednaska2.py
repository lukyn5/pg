



if __name__ == "__main__":
    #konverze na int
    hodnota1 = input("Zadej číslo: ")
    hodnota1 = int(hodnota1)
    
    operator = input("Zadej operator (+, -, *, /): ")
    #konverze na int
    hodnota2 = input("Zadej číslo: ")
    hodnota2 = int(hodnota2)
    # formatovany string (text)
    print (f"Operace: {hodnota1} {operator} {hodnota2} =")
    # nastavit "nic" dokud v promnene neni vysledek operace
    vysledek = None

    #vypocet

    #podminka složena z více vetvi if -ilif - ... - else
    if operator == "+":
        vysledek = hodnota1 + hodnota2

    elif operator == "-":
        vysledek = hodnota1 - hodnota2

    elif operator == "*":
        vysledek = hodnota1 * hodnota2
    
    elif operator == "/":
        if hodnota2 == 0:
            print("nelze dělit 0")
        else:
            vysledek = hodnota1 / hodnota2


    else:
        print("Neznámý operátor '{operator}'") 

    if vysledek == None:
        print("Operace se nezdařila")

    else:
        print(f"Vysledek operace: {vysledek}")



