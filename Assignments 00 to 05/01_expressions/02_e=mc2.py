def main():
    # Define the speed of light constant (C)
    C = 299792458  # meters per second

    # Prompt the user to enter mass in kilograms
    mass = float(input("Enter kilos of mass: "))

    # Calculate energy using E = m * C^2
    energy = mass * C**2

    # Display the results
    print("\ne = m * C^2...\n")
    print(f"m = {mass} kg")
    print(f"C = {C} m/s")
    print(f"{energy} joules of energy!")

# Ensures the script runs only when executed directly
if __name__ == "__main__":
    main()
