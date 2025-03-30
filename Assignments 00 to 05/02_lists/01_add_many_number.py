def sum_of_numbers(numbers):
    """Returns the sum of the given list of numbers."""
    return sum(numbers)

def main():
    # Example list of numbers
    numbers = [1, 2, 3, 4, 5]
    
    # Compute the sum and store the result
    total = sum_of_numbers(numbers)
    
    # Print the result
    print("The sum of the numbers is:", total)

    # Return the sum
    return total

# Ensures the script runs only when executed directly
if __name__ == '__main__':
    result = main()
