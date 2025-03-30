def main():
    MAX_VALUE = 10000  # Set the maximum limit

    # Initialize Fibonacci sequence
    a, b = 0, 1

    # Print Fibonacci numbers while they are less than MAX_VALUE
    while a < MAX_VALUE:
        print(a, end=" ")  # Print without a newline
        a, b = b, a + b  # Update values for next iteration

    print()  # Move to a new line after the sequence

# Required to run the main function
if __name__ == '__main__':
    main()
