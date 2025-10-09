

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


def naformatuj_text(zak):


    jmeno = zak['jmeno']
    primeni = zak['primeni']
    vek = zak['vek']
    obor = zak['obor']
    
    prm = round(sum(zak['znamky']) / len(zak['znamky']), 2)

    prt = ("Student: " + jmeno + " " + primeni + ", Vek: " + str(vek) + ", Obor: " + obor + ", Prumer: " + str(prm))

    return prt
    




if __name__ == "__main__":
    #seznam.append(["a", "b", "c"])

    #print(seznam[4][1])


 #   x = [1, 2]
  #  print(vrat_treti_prvek(x)) # vrati None

   # y = [12, 24, 56, 78]
   # print(vrat_treti_prvek(y)) # vrati 56

   # cisla = [1, 2, 3, 4, 5]
   # print(prumer(cisla))


   student = {
       "jmeno" : "Jan",
       "primeni" : "Novak",
       "vek" : 22,
       "znamky" : [1, 2, 3, 1, 2, 1],
   }
   student["vek"] += 1
   student["obor"] = "AEFP"
   print(naformatuj_text(student))