import random

def main():
    for _ in range(10):  # Loop 10 times
        print(random.randint(1, 100), end=" ")  # Print numbers on the same line
    
    print()  # Move to a new line after printing all numbers

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
