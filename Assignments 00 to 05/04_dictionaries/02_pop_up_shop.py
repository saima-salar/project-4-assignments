def main():
    # Fruit prices dictionary (fruit name → price per unit)
    fruit_prices = {
        "apple": 5.0,
        "durian": 15.0,
        "jackfruit": 10.0,
        "kiwi": 7.5,
        "rambutan": 8.0,
        "mango": 12.5
    }

    total_cost = 0  # Variable to store the total cost

    # Loop through each fruit and ask for the quantity
    for fruit, price in fruit_prices.items():
        while True:
            try:
                quantity = int(input(f"How many ({fruit}) do you want?: ").strip())
                if quantity < 0:
                    print("⚠ Please enter a non-negative number.")
                else:
                    break
            except ValueError:
                print("⚠ Invalid input! Please enter a number.")

        # Add the cost of the selected fruit to total
        total_cost += quantity * price

    # Display total cost
    print(f"\n💰 Your total is ${total_cost:.2f}")

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
