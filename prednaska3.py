if __name__ == "__main__":
    """"
    a = 0
    while a < 20:
        a += 1
        print(f"a je {a} a je mensi než 20")

    print("Bomba 💣")
    """
    """
    pozice_znaku_a = []
    text = list("ahoj, jak se mas?")

    for i, x in enumerate(text):
        if x == "a":
            pozice_znaku_a.append(i)

    print(pozice_znaku_a)

    for i in pozice_znaku_a:
        text[i] = "A"
    
    print(text)
    """

    jmeno = ["Alice", "Bob", "Eva"]
    vek = [25, 30, 22]
    for vek, jmeno in zip(vek, jmeno):
        print(f"{jmeno} je stary {vek} let")
