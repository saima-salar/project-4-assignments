def get_user_data():
    """Asks the user for their first name, last name, and email, then returns them."""
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email = input("What is your email address?: ")
    return first_name, last_name, email  # Return values as a tuple

def main():
    user_data = get_user_data()  # Get user data
    print("Received the following user data:", user_data)  # Print the tuple

if __name__ == '__main__':
    main()
