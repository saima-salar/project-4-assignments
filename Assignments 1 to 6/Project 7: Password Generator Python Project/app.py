import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input
try:
    length = int(input("🔐 Enter the length of your desired password: "))
    password = generate_password(length)
    print("✅ Your Generated Password: ", password)
except ValueError:
    print("⚠️ Please enter a valid number!")

