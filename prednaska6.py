#from p6_muj_modul import fibonacci
import random
import time

def hraci_automat():
    symboly = ["💩", "💀", "🤖", "🎉", "⭐", "🔥", "🌟"]
    random.seed(10)
    step = 0
    while True:
        step += 1
        vysledek = []
        for i in range(3):
            vysledek.append(random.choice(symboly))
        print(vysledek)
        if len(set(vysledek)) == 1:
            print(f"vyhrál jsi na {step} pokus!")
            break

if __name__ == "__main__":
    #fib = fibonacci(25)
    #print(list(reversed(fib)))

    ts = time.time() #začátek měření času - timestamp

    hraci_automat()

    print("čas běhu:", time.time() - ts, "sekund") #konec měření času