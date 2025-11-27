class ChybnyDatovyTyp(Exception):
    pass

class Osoba:
    def __init__(self, jmeno, telefon, email):
        self.jmeno = jmeno
        self.telefon = telefon
        self.email = email

    @property
    def jmeno(self):
        """Getter pro atribut jmeno."""
        return self.__jmeno

    @jmeno.setter
    def jmeno(self, nove_jmeno):
        """Setter pro atribut jmeno s validací."""
        
        # 1. Kontrola datového typu
        if not isinstance(nove_jmeno, str):
            raise ChybnyDatovyTyp('Jméno musí být textový řetězec (str).')
        
        # 2. Kontrola obsahu (pouze písmena a mezery)
        ciste_jmeno = nove_jmeno.replace(' ', '')
        
        if len(ciste_jmeno) == 0 or not ciste_jmeno.isalpha():
            raise ChybnyDatovyTyp('Jméno smí obsahovat pouze písmena a mezery.')

        # Pokud validace projde, uložíme hodnotu do interní proměnné.
        self.__jmeno = nove_jmeno

    def __str__(self):
        return f'Osoba({self.jmeno} ,{self.telefon}, {self.email})'
    

if __name__ == "__main__":
    
    try:
        # Toto vyvolá chybu, protože jsou tam čísla
        o1 = Osoba("12345", "+420777888999", "ahoj ahoj@email.cz")
        print(o1)
    except ChybnyDatovyTyp as e:
        print(f"Chyba: {e}")