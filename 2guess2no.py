import random

print("🎯 Welcome to Guess the Number Game!")

target = random.randint(1, 50)
attempts = 0

while True:
    guess = int(input("Enter your guess (1-50): "))
    attempts += 1
    
    if guess < target:
        print("Too Low! Try again.")
    elif guess > target:
        print("Too High! Try again.")
    else:
        print(f"🎉 Congratulations! You guessed it right in {attempts} attempts!")
        break
