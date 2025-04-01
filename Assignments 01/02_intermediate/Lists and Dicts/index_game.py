def access_element(lst, index):
    # Accessing an element at the specified index
    if index < 0 or index >= len(lst):
        return "Index out of range"
    return lst[index]

def modify_element(lst, index, new_value):
    # Modifying an element at the specified index
    if index < 0 or index >= len(lst):
        return "Index out of range"
    lst[index] = new_value
    return lst

def slice_list(lst, start, end):
    # Slicing the list from start to end index
    if start < 0 or end > len(lst):
        return "Invalid index range"
    return lst[start:end]

def game():
    # A list with different elements
    sample_list = ['apple', 42, 'banana', 7.8, 'orange']

    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':  # Access an element
            index = int(input("Enter the index to access: "))
            result = access_element(sample_list, index)
            print("Accessed element:", result)
        
        elif choice == '2':  # Modify an element
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            result = modify_element(sample_list, index, new_value)
            print("Updated list:", result)
        
        elif choice == '3':  # Slice the list
            start = int(input("Enter the start index: "))
            end = int(input("Enter the end index: "))
            result = slice_list(sample_list, start, end)
            print("Sliced list:", result)
        
        elif choice == '4':  # Exit
            print("Thanks for playing!")
            break
        
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    game()
