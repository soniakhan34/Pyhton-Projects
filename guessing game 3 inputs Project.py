import random


secret_number = random.randint(1, 20)

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 20.")
print("You have 3 chances to guess it.")


attempts = 3

for attempt in range(1, attempts + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed it right. The number was {secret_number}.")
        break
else:
    print(f"Sorry, you've used all your attempts. The number was {secret_number}.")
