import hashlib

def hash_password(password: str) -> str:
    """Hashes a given password using SHA256."""
    return hashlib.sha256(password.encode()).hexdigest()

def login(email: str, password_to_check: str, stored_logins: dict) -> bool:
    """
    Verifies if the provided password matches the stored hashed password for a given email.
    
    Parameters:
        email (str): The user's email.
        password_to_check (str): The password to be verified.
        stored_logins (dict): A dictionary containing email-password_hash pairs.
    
    Returns:
        bool: True if the password matches, False otherwise.
    """
    # Hash the password to check
    hashed_input_password = hash_password(password_to_check)
    
    # Compare with stored hash (if email exists in the dictionary)
    return stored_logins.get(email) == hashed_input_password

def main():
    # Simulating a database of stored hashed passwords
    stored_logins = {
        "user1@example.com": hash_password("password123"),
        "user2@example.com": hash_password("mysecurepassword"),
        "user3@example.com": hash_password("helloWorld!"),
    }

    # Get user input
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()

    # Authenticate user
    if login(email, password, stored_logins):
        print("✅ Login successful!")
    else:
        print("❌ Invalid email or password.")

# Required to run the main function
if __name__ == '__main__':
    main()
