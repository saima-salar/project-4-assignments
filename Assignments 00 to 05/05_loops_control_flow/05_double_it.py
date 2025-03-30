def main():
    curr_value = int(input("Enter a number: "))  # Get the initial number from user

    while curr_value < 100:  # Continue doubling until 100 or greater
        curr_value *= 2  # Double the value
        print(curr_value, end=" ")  # Print result on the same line

# Required to run the main function
if __name__ == '__main__':
    main()
