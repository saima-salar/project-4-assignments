import random

def main():
    # Randomly select a number between 0 and 99
    number_to_guess = random.randint(0, 99)
    
    while True:
        guess = int(input("Enter a guess: "))
        
        if guess < number_to_guess:
            print("Your guess is too low")
        elif guess > number_to_guess:
            print("Your guess is too high")
        else:
            print(f"Congrats! The number was: {number_to_guess}")
            break  # Exit the loop when the correct guess is made

if __name__ == '__main__':
    main()
