# Phone Contact Project

contacts = {}  # Empty dictionary to store contacts

def add_contact():
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    contacts[name] = number
    print(f"Contact '{name}' added successfully!\n")

def view_contacts():
    if contacts:
        print("\n--- All Contacts ---")
        for name, number in contacts.items():
            print(f"{name}: {number}")
        print()
    else:
        print("No contacts found.\n")

def remove_contact():
    name = input("Enter the name of the contact to remove: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' removed successfully!\n")

    else:
        print(f"No contact found with the name '{name}'.\n")

def delete_all_contacts():
    confirm = input("Are you sure you want to delete all contacts? (yes/no): ").lower()
    if confirm == 'yes':
        contacts.clear()
        print("All contacts have been deleted!\n")

    else:
        print("Operation cancelled.\n")

def main():
    while True:
        print("Phone Contact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Delete All Contacts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_contact()

        elif choice == '2':
            view_contacts()

        elif choice == '3':
            remove_contact()

        elif choice == '4':
            delete_all_contacts()

        elif choice == '5':
            print("Exiting Phone Contact Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please select between 1-5.\n")


if __name__ == "__main__":
    main()
