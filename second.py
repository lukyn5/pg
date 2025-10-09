def cislo_text(cislo):

    # určení čísel
    prvni = ['nula', 'jedna', 'dva', 'tři', 'čtyři', 'pět', 'šest', 'sedm', 'osm', 'devět']
    druha = ['dvacet', 'třicet', 'čtyřicet', 'patesát', 'šedesát', 'sedmdesát', 'osmdesát', 'devadesát'] # -2
    nact = ['deset', 'jedenáct', 'dvanáct', 'třináct', 'čtrnáct', 'patnáct', 'šestnáct', 'sedmnáct', 'osmnáct', 'devatenáct']

    # definování indexu posledního čísla
    jednotky = int(str(cislo)[-1])

    if cislo < 10:
        return prvni[jednotky]
    
    elif 10 <= cislo < 20:
        # definování indexu čísel mezi 10 a 20
        nactcs = int(cislo) - 10
        return nact[nactcs]
    
    elif 20 <= cislo < 100:
        # definování indexu u desítek (-2 protože začínáme od 20)
        desitky = int(str(cislo)[-2]) -2
        if jednotky == 0:
            return druha[desitky]
        else:
            return druha[desitky] + " " + prvni[jednotky]
        
    if cislo == 100:
        return "sto"
    if cislo > 100:
        print ("Nelze zadat větší číslo než 100")

 

if __name__ == "__main__":
    cislo = int(input("Zadej číslo: "))
    text = cislo_text(cislo)
    print(text)