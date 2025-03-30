def add_three_copies(lst, data):
    """Adds three copies of 'data' to the given list 'lst'."""
    lst.append(data)
    lst.append(data)
    lst.append(data)

def main():
    # Get user input
    message = input("Enter a message to copy: ")

    # Create an empty list
    my_list = []

    print("List before:", my_list)

    # Modify the list inside the function (changes persist due to mutability)
    add_three_copies(my_list, message)

    print("List after:", my_list)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
