def main():
    number_counts = {}  # Dictionary to store number occurrences
    
    while True:
        num = input("Enter a number (or press enter to stop): ")  
        if num == "":  # Stop when the user presses enter without input
            break
        
        num = int(num)  # Convert input to integer
        if num in number_counts:
            number_counts[num] += 1  # Increment count if number exists
        else:
            number_counts[num] = 1  # Initialize count if number is new

    print("\nOccurrences:")
    for num, count in number_counts.items():
        print(f"{num} appears {count} time{'s' if count > 1 else ''}.")

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()


