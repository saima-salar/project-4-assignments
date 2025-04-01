import random

print("Guess the number between 1 and 100!")

# Generate random number
number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Enter your guess: "))  # Fixed input prompt
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue  # Skip the rest of the loop and ask for input again

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You got it right!")
        break  # Exit loop when guessed correctly

