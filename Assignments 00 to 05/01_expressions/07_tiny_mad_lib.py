def main():
    # Constant sentence start
    SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"

    # Get user inputs
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")

    # Print the final sentence
    print(f"{SENTENCE_START} {adjective} {noun} {verb}!")

# Ensures the script runs only when executed directly
if __name__ == '__main__':
    main()
