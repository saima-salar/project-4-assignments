def main():
    values = []  # Initialize an empty list
    
    while True:
        user_input = input("Enter a value: ")
        
        if user_input == "":  # If the input is empty, break the loop
            break
        
        values.append(user_input)  # Add the input to the list

    print("Here's the list:", values)  # Print the final list

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
