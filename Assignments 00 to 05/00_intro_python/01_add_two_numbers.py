def main():
    """Function to take two integer inputs and print their sum."""
    print("This program adds two numbers.")

    # Prompt the user to enter the first number
    num1: str = input("Enter first number: ")
    num1 = int(num1)

    # Prompt the user to enter the second number
    num2: str = input("Enter second number: ")
    num2 = int(num2)

    # Calculate the sum
    total_sum = num1 + num2

    # Print the result
    print("The total is " + str(total_sum) + ".")

# Ensure the function runs only if the script is executed directly
if __name__ == "__main__":
    main()
