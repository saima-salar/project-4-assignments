def find_average(num1, num2):
    return (num1 + num2) / 2  # Calculate the average

def main():
    # Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Call function and print result
    average = find_average(num1, num2)
    print(f"The average of {num1} and {num2} is {average}")

# Required to run the main function
if __name__ == '__main__':
    main()
