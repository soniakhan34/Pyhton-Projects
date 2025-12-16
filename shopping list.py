#**Shopping List Application**     
#Write a Python program to create a shopping list. The program should allow the user to:
#1. Add items to the list.
#2. Remove items from the list.
#3. View all items in the list.
#4. Exit


#------------------------------Shopping list----------------------------------

shopping_list = []

while True:
    print("/n----------Shopping list Menu----------")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Item")
    print("4. Exist")

    choice =input("Enter your choice (1-4) :")

    if choice == "1":
        item = input("Enter item to add:")
        shopping_list.append(item)
        print(f"'(item)' added to the list ")


    elif choice == "2":
        item = input("Enter item to remove:")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'(item)' removed from the list.")
        else:
            print("Item not found in the list.")

    elif choice == "3":
        if len(shopping_list) == 0:
            print("Your shopping list is empty.")
        else:
            print("\nYour Shopping List:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")

    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
