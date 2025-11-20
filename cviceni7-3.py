class ChybaCastky(Exception):
    pass



class BankovniUcet:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.__zustatek = 0

    def vloz(self, suma):
        if suma <= 0:
            raise ChybaCastky("Nelze pridat nulovou nebo zapornou částku")
        
        self.__zustatek += suma

    def vyber(self, suma):

            if suma <= 0:
                raise ChybaCastky("Nelze pridat nulovou nebo zapornou částku")
            if suma > self.__zustatek:
                raise ChybaCastky("Nelze VYBRAT VÍCE než je na ")
            self.__zustatek -= suma 

    def __str__(self):
        
        return f'Ucet vlastní {self.jmeno} a je na něm {self.__zustatek} Kč'
    
if __name__ == "__main__":
    ucet = BankovniUcet("Alice")
    print(ucet)

    try:
        ucet.vloz(100)
    except ChybaCastky as e:
        print(f"Chyba: {e}")
    print(ucet)

    try:
        ucet.vyber(50)
    except ChybaCastky as e:
        print(f"Chyba: {e}")
    print(ucet)

    try:
        ucet.vloz(10)
    except ChybaCastky as e:
        print(f"Chyba: {e}")
    print(ucet)

    try:
        ucet.vyber(60)
    except ChybaCastky as e:
        print(f"Chyba: {e}")
    print(ucet)

