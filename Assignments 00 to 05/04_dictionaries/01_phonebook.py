def main():
    phonebook = {}  # Dictionary to store contacts

    while True:
        print("\n📞 Phonebook Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. View All Contacts")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":  # Add a new contact
            name = input("Enter contact name: ").strip()
            number = input("Enter phone number: ").strip()
            phonebook[name] = number
            print(f"✅ {name} has been added.")

        elif choice == "2":  # Search for a contact
            name = input("Enter contact name to search: ").strip()
            if name in phonebook:
                print(f"📞 {name}'s number: {phonebook[name]}")
            else:
                print("❌ Contact not found!")

        elif choice == "3":  # View all contacts
            if not phonebook:
                print("📭 Phonebook is empty!")
            else:
                print("\n📋 Contacts List:")
                for name, number in phonebook.items():
                    print(f"{name}: {number}")

        elif choice == "4":  # Exit program
            print("👋 Exiting phonebook. Have a great day!")
            break

        else:
            print("⚠ Invalid option! Please choose a valid number (1-4).")

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
