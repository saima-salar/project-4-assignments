def subtract_seven(num):
    """Subtracts 7 from the given number."""
    return num - 7

def main():
    num = int(input("Enter a number: "))  # Take input from user
    result = subtract_seven(num)  # Call the function
    print("Result after subtracting 7:", result)  # Print result

if __name__ == '__main__':
    main()
