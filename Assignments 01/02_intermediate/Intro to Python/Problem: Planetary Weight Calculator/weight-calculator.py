import random

def mars_weight():
    # Milestone #1: Mars Weight Calculation
    earth_weight = float(input("Enter a weight on Earth: "))
    mars_weight = earth_weight * 0.378
    mars_weight = round(mars_weight, 2)
    print(f"The equivalent on Mars: {mars_weight}")

def planetary_weight():
    # Milestone #2: Weight Calculation for Any Planet
    planet_gravity = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    earth_weight = float(input("Enter a weight on Earth: "))
    planet_name = input("Enter a planet: ")

    if planet_name in planet_gravity:
        planet_weight = earth_weight * planet_gravity[planet_name]
        planet_weight = round(planet_weight, 2)
        print(f"The equivalent weight on {planet_name}: {planet_weight}")
    else:
        print("Invalid planet name. Please enter a valid planet from the list.")

def main():
    print("Choose the milestone you want to run:")
    print("1. Mars Weight Calculation")
    print("2. Planetary Weight Calculation")
    choice = int(input("Enter 1 or 2: "))
    
    if choice == 1:
        mars_weight()
    elif choice == 2:
        planetary_weight()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
