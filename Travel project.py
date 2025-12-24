print("----------------Welcome to Smart Travel Planner Project---------------------")

try:
    ##----------------------------City Selection------------------------------
    print("\n------------------------Select City:----------------------------")
    print("1.Karachi")
    print("2. Hyderabad")
    print("3. Islamabad")

    city_choice=int(input("Enter city number:"))
    if city_choice==1:
        city ="Karachi"

    elif city_choice==2:
        city ="Hyderabad"

    elif city_choice==3:
        city ="Islamabad"

    else:
        print("Invalid city selection!")
        exit()

    

    ##------------------------Transport Selection-----------------------------

    print("\n----------------------Select Transport:--------------------------")
    print("1. Bus")
    print("2. Taxi")
    print("3. Metro / Train")

    transport_choice=int(input("Enter transport number: "))

    if transport_choice == 1:
        transport = "Bus"
        fare = 50
        
    elif transport_choice == 2:
        transport = "Taxi"
        fare = 100
        
    elif transport_choice == 3:
        transport = "Metro"
        fare = 80
        
    else:
        print("Invalid transport selection!")
        exit()

    
    time_slot=input("\nEnter preferred time slot 'morning' / 'afternoon' / 'evening'): ").lower()

    valid_slot=False

    if transport=="Bus":
        if time_slot == "morning" or time_slot=="evening":
            valid_slot = True

    elif transport == "Taxi":
        if time_slot in ['morning', 'afternoon', 'evening']:
            valid_slot = True

    elif transport == "Metro":
        if time_slot == 'afternoon' or time_slot == 'evening':
            valid_slot = True

    if not valid_slot:
        print("Selected time slot is not available for this transport.")
        exit()

    
    budget=int(input("\nEnter your budget: "))

    if budget < fare:
        print("Insufficient budget!")
        exit()

    total_cost=fare

    
    extra=input("\nDo you want extra services? (yes/no): ").lower()

    if extra == "yes":
        print("\n--------------------Select Extra Service:-----------------------------")
        print("1. Meal (20)")
        print("2. Guide (30)")
        print("3. Priority Boarding (40)")

        service_choice = int(input("Enter service number: "))

        if service_choice == 1:
            total_cost += 20

        elif service_choice == 2:
            total_cost += 30

        elif service_choice == 3:
            total_cost += 40

        else:
            print("Invalid service choice!")

    
    print('\n------------------------Travel Summary----------------------------------')
    print("City:", city)
    print("Transport:", transport)
    print("Time Slot:", time_slot.capitalize())
    print("Total Cost:", total_cost)
    print("Trip planned successfully!")
    print("Thank you for Smart Travel Planner..................")
except ValueError:
    print("Invalid input! Please enter correct values.")
