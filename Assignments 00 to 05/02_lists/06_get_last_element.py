def get_last_element(lst):
    """Prints the last element of the given list."""
    print("The last element is:", lst[-1])  # Access the last element using negative indexing

def main():
    # Get the number of elements in the list
    n = int(input("Enter the number of elements in the list: "))

    # Initialize an empty list
    my_list = []

    # Get list elements from the user
    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        my_list.append(element)

    # Call the function to print the last element
    get_last_element(my_list)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
