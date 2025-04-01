import random

def guess_the_number():
    """Project 2: Guess the Number Game Python Project (computer)"""
    number = random.randint(1, 100)
    guesses_left = 7

    # Welcome message
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    # Loop to handle guesses
    while guesses_left > 0:
        print(f"\nYou have {guesses_left} guesses left.")

        try:
            guess = int(input("Take a guess: "))  # Fixed prompt wording
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue  # Skip the rest of the loop and ask for input again

        # Check if the guess is correct
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {7 - guesses_left + 1} tries.")
            return  # Exit function if guessed correctly

        guesses_left -= 1  # Decrement guess count

    # If out of guesses
    print(f"\nYou ran out of guesses. The correct number was {number}.")

# Run the game
guess_the_number()

