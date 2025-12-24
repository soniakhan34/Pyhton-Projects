##------------------------------Sonia Hotel------------------------------------------
#---------------------Smart Restaurant Ordering system---------------------------------

menu={'Fast Food':{'Burger': 150, 'Pizza': 300},'BBQ': {'Tikka': 200, 'Boti': 250},'Chinese': {'Chowmein': 180, 'Fried Rice': 220}}

while True:
    print('\n---------Welcome to Sonia Royal Smart Restaurant Ordering System-----------------')
    print('----------Please follow the steps to place your order.\n----------------------------')

    
    while True:
        print("Select Food Category:")
        print("1. Fast Food")
        print("2. BBQ")
        print("3. Chinese")

        category_choice=input("Enter choice: ")

        if category_choice=="1":
            category="Fast Food"
            break

        elif category_choice=="2":
            category="BBQ"
            break

        elif category_choice=="3":
            category="Chinese"
            break

        else:
            print("Invalid category. Please try again.\n")

    
    while True:
        print(f"\nAvailable items in {category}:")
        items=list(menu[category].items())


        for i in range(len(items)):
            print(f'{i+1}. {items[i][0]} ({items[i][1]})')

        item_choice=input("Select item: ")


        if item_choice.isdigit() and 1 <= int(item_choice) <= len(items):
            item_name=items[int(item_choice) - 1][0]
            item_price=items[int(item_choice) - 1][1]
            break

        else:
            print("Invalid item selection. Try again.")

    
    while True:

        try:
            quantity=int(input("Enter quantity: "))

            if quantity > 0:
                break

            else:
                print("Quantity must be greater than 0.")


        except ValueError:
            print("Please enter a valid number.")

    subtotal=item_price*quantity

   
    add_on_cost=0
    add_on_name="None"

    add_on =input("Do you want add-ons? (yes/no): ").lower()

    if add_on=="yes":
        print("1. Extra Cheese (50)")
        print("2. Drink (60)")
        print("3. Both")

        choice=input("Select add-on option: ")

        if choice=="1":
            add_on_cost=50
            add_on_name="Extra Cheese"

        elif choice=="2":
            add_on_cost=60
            add_on_name="Drink"

        elif choice=="3":
            add_on_cost=110
            add_on_name="Extra Cheese + Drink"

        else:
            print("Invalid add-on choice. No add-ons added.")

    grand_total=subtotal + add_on_cost

   
    print('\n----------------Order Summary----------------------')
    print('Food Category :', category)
    print('Item          :', item_name)
    print('Price         :', item_price)
    print('Quantity      :', quantity)
    print('Subtotal      :', subtotal)
    print('Add-ons       :', add_on_name)
    print('Add-on Cost   :', add_on_cost)
    print('------------------------------------------------------')
    print('Grand Total   :', grand_total)
    print('Thank you for ordering')

   
    again=input("\nDo you want to place another order? (yes/no): ").lower()

    if again!="yes":
        print("Program ended.")
        break

