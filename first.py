def sudy_nebo_lichy(cislo):
    if cislo % 2 == 0:
        return True
    else:
        return False
    


if __name__ == "__main__":
    if sudy_nebo_lichy(5) == True:
        print("Je sudé")
    else:
        print("Je liché")