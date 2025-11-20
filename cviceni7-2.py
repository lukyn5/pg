class Osoba:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def __str__(self):
        return f'Osoba: {self.jmeno} má {self.vek} let'
    
    def pridat_rok(self):
        pass
    
class Student(Osoba):
    def __init__(self, jmeno, vek, rocnik=1):
        super().__init__(jmeno, vek)
        self.rocnik = rocnik

    def __str__(self):
        return f'Student: {self.jmeno} studuje {self.rocnik}. rocnik a je mu {self.vek} let'
    
    def pridat_rok(self):
        super().pridat_rok()
        if self.rocnik >= 5:
            raise Exception("Už jsme na konci studia")
        self.rocnik += 1


class Ucitel(Osoba):

    def __init__(self, jmeno, vek, praxe=0):
        super().__init__(jmeno, vek)
        self.praxe = praxe

    def __str__(self):
        return f'Učitel: {self.jmeno} má {self.praxe} let praxe a je mu {self.vek} let'
    pass

    def pridat_rok(self):
        self.praxe += 1



if __name__ == "__main__":
    student1 = Student("Alice", 19)
    student2 = Student("Bob", 27, 2)

    ucitel1 = Ucitel("Prof", 45 , 5)

    udrzbar1 = Osoba("Karel", 55)

    print(student1)
    print(student2)
    print(ucitel1)

    for i in range(3):
        try:
            student1.pridat_rok()
        except Exception as e:
            print(f"Chyba: {e}")
            break
    print(student1)


    for i in range(5):
        ucitel1.pridat_rok()

    print(ucitel1)

    osoby = [student1, student2, ucitel1, udrzbar1]
    for osoba in osoby:
        for i in range(10):
            try:
                osoba.pridat_rok()
            except Exception as e:
                break

    print(student1)
    print(student2)
    print(ucitel1)

    print(udrzbar1)