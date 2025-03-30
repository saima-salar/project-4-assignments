def main():
    # Prompt the user to enter a value in feet
    feet = float(input("Enter the length in feet: "))

    # Conversion factor: 1 foot = 12 inches
    inches = feet * 12

    # Print the result
    print(f"{feet} feet is equal to {inches} inches.")

# Ensures the script runs only when executed directly
if __name__ == "__main__":
    main()
