#contact list app


contacts={}  #creating dictionary to addd name and number 


while True:

    print('''----Options-----
1-Add Contact
2-View Contacts
3-Search Contact
4-Remove Contact
5-Edit Contact
6-Edit Number
7-Exit ''')

    option=input("Enter your Option (1-7):  ")
    #if number one selected  1-add contact
    if option == "1":
       name=input("Enter name: ").strip()
       phone=input("Enter phone number:  ").strip()


       if name in contacts:
           print(f"This contact already exists {name}: {contacts[name]}")
           
       else:
           
           contacts[name]=phone

           print(f"name: {name}: phone {phone} added succesfully! ")



    #2-view contacts
    elif option =="2":
        if len(contacts)==0: #if no contact in file
            print("No contacts in the file!")
            
        else:  #if contacts in contacts file
            print("-----Total Contacts----")
            
            for name,phone in contacts.items():    
                print(f"{name}:{phone}")




    #3-search contact

    elif option == "3":
        if len(contacts)==0:  #if  no contacts in contactt file
            print("No contact to search! ")

        else:
            name=input("Enter name to search:   ").strip()

            if name not in contacts:  #if searched name in not contact file
                print(f"{name}: Not found!")

            elif name in contacts:
                print(f"{name}:{contacts[name]}")  #if searched name in contact file


                
    #4-remove contacts
    elif option =="4":
        if len(contacts)==0: #if length of contact file is zero  (mean no contact in file)
            print("No contact to remove!")

        else:
            name=input("Enter name you wanna remove:  ").strip()

            if name in contacts:
                sure_remove=input("Are you sure deleting name! (y/n):   ").strip()
                sure_remove=sure_remove.lower()

                if sure_remove !="y":
                    print(f"Okay Not deleting name! {name} ")  #if user confirms not by writes (n)
                    
                elif sure_remove =="y":    # if user confirms by writing y 
                    removed_name=contacts.pop(name)
                    print(f"{name}: {removed_name}  has been deleted!")

                else:
                    print("Invalid Character! Try again!")
            else:
                print(f"{name}: not found to remove!")


    #edit name             
    elif option=="5":
        if len(contacts)==0:
            print("No contact name to edit!")   #if no contact name in list

        else:
            old_name=input("Enter old name to edit:  ").strip()     #accessing old name by user to edit

            if old_name in contacts:    #if old name in contacts file
        
                new_name=input("Enter new name:  ").strip()  #accessing new name by user to change name

                if new_name in contacts:  #if new_name already exists in contacts file 
                    print(f"New name: {new_name} already exists in contacts file!  ")

                else:
                    contacts[new_name]=contacts[old_name]  #copying phone to new_name
                    del contacts[old_name]

                print(f"{new_name}:{contacts[new_name]}  edited successfully!")

                
    #6-edit number!            
    elif option =="6":
        if len(contacts)==0:
            print("No Contact Number to edit! ")

        else:
            
            name=input("Search Name to edit number:  ").strip()

            if name in contacts:
                phone=input("enter number to add : ").strip()  #accessing number to add to , name
                contacts[name]=phone  #adding phone number to the searched name

                print(f"number: {contacts[name]} added successfully! ")

            else:
                print(f"{name}: not found to edit number! ")
        

    #7- exit() 
    elif option =="7":
        print("Exiting...")
        exit()


    else:
        print("Invalid Option!")











