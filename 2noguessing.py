import random

def guess_game():
    number = random.randint(1, 50)  # random number between 1 and 50
    attempts = 0

    print("🎲 Welcome to the Number Guessing Game!")
    print("I have picked a number between 1 and 50. Can you guess it?")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed the number {number} in {attempts} attempts.")
            break

guess_game()
