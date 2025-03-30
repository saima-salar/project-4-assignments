def main():
    MIN_HEIGHT = 50  # Minimum height requirement

    while True:
        height = input("How tall are you? (Press Enter to quit): ")

        # Exit if the user does not enter a value
        if height == "":
            print("Goodbye!")
            break
        
        height = int(height)  # Convert input to an integer

        if height >= MIN_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
