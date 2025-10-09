

def prace_se_seznamem():


    seznam = [100, 5, 3, 21]

    #vezme 3. prvek a vynásobí ho 2x
    seznam[2] *= 2
    #na konci seznamu přidat nový prvek
    seznam.append(55)
    #seznam setridime vzestupne
    seznam.sort()
    #otoč pořadí prvku v seznamu
    seznam.reverse()

    print(seznam)

def vrat_treti_prvek(seznam):
    
    if len(seznam) >= 3:
        return seznam[2]
    else:
        return None
    
def prumer(cisla):
    return sum(cisla) / len(cisla)
    




if __name__ == "__main__":
    #seznam.append(["a", "b", "c"])

    #print(seznam[4][1])


 #   x = [1, 2]
  #  print(vrat_treti_prvek(x)) # vrati None

   # y = [12, 24, 56, 78]
   # print(vrat_treti_prvek(y)) # vrati 56




    cisla = [1, 2, 3, 4, 5]
    print(prumer(cisla))