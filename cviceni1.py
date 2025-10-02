def main():
    vstup = input("zadej číslo: ")
    vstup = int(vstup)
    vstup *= 3
    vstup -= 2

    if vstup > 10:
        print("větší než 10")

    else:
        print("mendsi")

    print(f"trojnásobek5 čísla je {vstup}")

if __name__ == "__main__":
    main()