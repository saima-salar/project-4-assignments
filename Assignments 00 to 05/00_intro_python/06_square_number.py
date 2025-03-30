def main():
    # Prompt the user for a number
    num = float(input("Type a number to see its square: "))

    # Print the result using f-string for better readability
    print(f"{num} squared is {num ** 2}")


# Ensures the script runs only when executed directly
if __name__ == "__main__":
    main()
