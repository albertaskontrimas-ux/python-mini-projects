import random

print("🎮 Welcome to the game!")
print("Guess a number from 1 to 10")
print("You have 3 attempts")

number = random.randint(1, 10)

for i in range(3):
    guess = int(input("Your guess: "))

    if guess == number:
        print("🔥 You win!")
        break
    else:
        print("❌ Try again")

print("Correct number was:", number)