def main():
    # Assign ages based on the problem statement
    Anton = 21  # Anton's age is given as 21 years old
    Beth = Anton + 6  # Beth is 6 years older than Anton
    Chen = Beth + 20  # Chen is 20 years older than Beth
    Drew = Chen + Anton  # Drew is as old as Chen's age plus Anton's age
    Ethan = Chen  # Ethan is the same age as Chen

    # Print out the ages in the required format
    print("Anton is", str(Anton))
    print("Beth is", str(Beth))
    print("Chen is", str(Chen))
    print("Drew is", str(Drew))
    print("Ethan is", str(Ethan))


# This ensures the script runs only when executed directly
if __name__ == "__main__":
    main()
