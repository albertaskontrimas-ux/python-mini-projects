print("1 - Calculator")
print("2 - Guess game")

choice = input("Choose: ")

if choice == "1":
    a = float(input("A: "))
    b = float(input("B: "))
    print("Result:", a + b)

elif choice == "2":
    import random
    number = random.randint(1, 10)
    guess = int(input("Guess: "))

    if guess == number:
        print("Win!")
    else:
        print("Lose. Number was:", number)