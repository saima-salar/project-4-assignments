MAX_LENGTH = 3  # Define the maximum length of the list

def shorten(lst):
    while len(lst) > MAX_LENGTH:  # Keep removing until the list is MAX_LENGTH
        removed_item = lst.pop()  # Remove the last item
        print("Removed:", removed_item)  # Print removed item

def main():
    lst = input("Enter list elements separated by spaces: ").split()  # Get user input as a list
    print("Original List:", lst)
    shorten(lst)  # Call the shorten function
    print("Final List:", lst)  # Print the modified list

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()

