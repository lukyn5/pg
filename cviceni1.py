def main():
    vstup = input("zadej číslo: ")
    vstup = int(vstup)
    vstup *= 3
    vstup -= 2

    if vstup > 10:
        print(f"Číslo {vstup} větší než 10")
    elif vstup < 10:
        print(f"Číslo {vstup} je menší než 10")
    else:
        print(f"Číslo {vstup}je to 10")


if __name__ == "__main__":
    main()