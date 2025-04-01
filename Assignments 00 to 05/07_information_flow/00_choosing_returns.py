ADULT_AGE = 18  # Define the adult age threshold

def is_adult(age):
    return age >= ADULT_AGE  # Return True if age is 18 or older, otherwise False

def main():
    age = int(input("How old is this person?: "))  # Take input from user
    print(is_adult(age))  # Print the result of is_adult function

if __name__ == '__main__':
    main()
