import random

def main():
    # Simulate rolling two dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    # Calculate the total
    total = die1 + die2

    # Print results
    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total: {total}")

# Ensures the script runs only when executed directly
if __name__ == '__main__':
    main()
