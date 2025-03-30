def main():
    affirmation = "I am capable of doing anything I put my mind to."
    
    while True:
        user_input = input("Please type the following affirmation: I am capable of doing anything I put my mind to.\n")
        
        if user_input == affirmation:
            print("That's right! :)")
            break  # Exit the loop when the correct input is given
        else:
            print("Hmmm That was not the affirmation. Try again.")

# Required to run the main function
if __name__ == '__main__':
    main()
