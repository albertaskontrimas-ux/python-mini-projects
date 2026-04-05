import random

while True:
    atstumas = random.randint(1, 100)

    if atstumas < 20:
        print("🛑 Kliūtis! Sukasi")
    else:
        print("➡️ Važiuoja")

    input("...")