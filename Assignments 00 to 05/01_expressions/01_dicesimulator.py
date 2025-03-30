import random  # Import the random module to generate random numbers

def roll_dice():
    """Simulates rolling a single die (1 to 6)."""
    return random.randint(1, 6)

def main():
    # Simulate rolling two dice three times
    for i in range(3):
        die1 = roll_dice()
        die2 = roll_dice()
        print(f"Roll {i + 1}: {die1}, {die2}")

# Ensures the script runs only when executed directly
if __name__ == "__main__":
    main()
