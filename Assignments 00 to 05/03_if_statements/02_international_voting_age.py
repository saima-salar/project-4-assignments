def main():
    # Ask user for their age
    age = int(input("How old are you? "))

    # Check voting eligibility for each country
    if age >= 16:
        print("You can vote in Peturksbouipo where the voting age is 16.")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is 16.")
    
    if age >= 25:
        print("You can vote in Stanlau where the voting age is 25.")
    else:
        print("You cannot vote in Stanlau where the voting age is 25.")
    
    if age >= 48:
        print("You can vote in Mayengua where the voting age is 48.")
    else:
        print("You cannot vote in Mayengua where the voting age is 48.")

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
