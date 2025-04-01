def greet(name):
    print(f"Greetings {name}!")  # Print a greeting message

def main():
    name = input("What's your name? ")  # Take input from user
    greet(name)  # Call the greet function

if __name__ == '__main__':
    main()
