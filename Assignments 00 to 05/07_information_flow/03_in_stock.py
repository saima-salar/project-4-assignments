def num_in_stock(fruit):
    """Returns the number of the given fruit in stock."""
    inventory = {
        "apple": 50,
        "banana": 30,
        "orange": 20,
        "pear": 1000,
        "grape": 15
    }
    return inventory.get(fruit.lower(), 0)  # Return stock count, default to 0 if not found

def main():
    fruit = input("Enter a fruit: ")  # Take input for fruit name
    stock = num_in_stock(fruit)  # Get stock count
    
    if stock > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock)
    else:
        print("This fruit is not in stock.")

if __name__ == '__main__':
    main()
