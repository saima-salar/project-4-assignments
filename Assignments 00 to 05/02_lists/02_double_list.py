def double_numbers(numbers):
    """Returns a new list with each number doubled."""
    return [num * 2 for num in numbers]

def main():
    # Example list of numbers
    numbers = [1, 2, 3, 4]
    
    # Double each element
    doubled_numbers = double_numbers(numbers)
    
    # Print the result
    print("Doubled numbers:", doubled_numbers)

    # Return the new list
    return doubled_numbers

# Ensures the script runs only when executed directly
if __name__ == '__main__':
    result = main()
