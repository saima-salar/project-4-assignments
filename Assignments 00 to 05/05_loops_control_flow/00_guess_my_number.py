import random

def main():
    # Generate a random number between 0 and 99
    secret_number = random.randint(0, 99)

    print("I am thinking of a number between 0 and 99...")

    while True:
        try:
            # Take user input
            guess = int(input("Enter a guess: "))

            # Check if the guess is correct
            if guess < secret_number:
                print("Your guess is too low")
            elif guess > secret_number:
                print("Your guess is too high")
            else:
                print(f"🎉 Congrats! The number was: {secret_number}")
                break  # Exit the loop when the guess is correct
        except ValueError:
            print("⚠ Please enter a valid number.")

# Required to run the main function
if __name__ == '__main__':
    main()
