def in_range(n, low, high):
    """Returns True if n is between low and high, inclusive."""
    return low <= n <= high  # Check if n is in the given range

def main():
    n = int(input("Enter a number: "))  # Take input for number
    low = int(input("Enter the lower bound: "))  # Take input for lower bound
    high = int(input("Enter the upper bound: "))  # Take input for upper bound
    print(in_range(n, low, high))  # Print the result of in_range function

if __name__ == '__main__':
    main()