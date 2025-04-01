def print_ones_digit(num):
    ones_digit = num % 10  # Get the ones digit using modulo operator
    print(f"The ones digit is {ones_digit}")

def main():
    num = int(input("Enter a number: "))  # Take input from user
    print_ones_digit(num)  # Call the function with user input

if __name__ == '__main__':
    main()
