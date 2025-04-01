import random

NUM_ROUNDS = 5  # You can adjust the number of rounds here

def main():
    score = 0  # Initialize score
    
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        
        # Generate random numbers for the player and the computer
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        
        print(f"Your number is {player_number}")
        
        # Get player's guess
        guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
        
        # Ensure the user enters a valid guess
        while guess not in ['higher', 'lower']:
            guess = input("Please enter either 'higher' or 'lower': ").strip().lower()

        # Game logic to check if the player's guess is correct
        if guess == "higher" and player_number > computer_number:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        elif guess == "lower" and player_number < computer_number:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        print(f"Your score is now {score}")
        print()  # Blank line after each round

    # Conditional ending messages
    print("Thanks for playing!")
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == '__main__':
    main()
