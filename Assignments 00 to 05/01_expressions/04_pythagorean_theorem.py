import math  # Import math module for square root function

def main():
    # Prompt the user to enter the lengths of the two perpendicular sides
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    # Calculate the hypotenuse using the Pythagorean theorem
    bc = math.sqrt(ab**2 + ac**2)

    # Print the result
    print(f"The length of BC (the hypotenuse) is: {bc}")

# Ensures the script runs only when executed directly
if __name__ == "__main__":
    main()
