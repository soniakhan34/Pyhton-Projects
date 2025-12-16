#Continue building the to-do list project by adding the following features:
#- Allow the user to mark tasks as completed and view only completed or pending tasks. - Add a feature to delete a to-do list entirely.


#----------------------------------------To---Do------List---------------------------------------------------------------------
todo_list = []
while True:
    print("\n--------To-Do-List-Menu----------")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. View All Tasks")
    print("4. View Completed Tasks")
    print("5. View Pending Tasks")
    print("6. Delete Entire To-Do List")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

   
    if choice == "1":
        task = input("Enter task to add: ")
        todo_list.append({"task": task, "completed": False})
        print(f"Task '{task}' added.")

    
    elif choice == "2":
        if len(todo_list) == 0:
            print("No tasks available to mark.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(todo_list, 1):
                status = "✔" if t["completed"] else "✘"
                print(f"{i}. {t['task']} [{status}]")

            num = int(input("Enter task number to mark completed: "))

            if 1 <= num <= len(todo_list):
                todo_list[num - 1]["completed"] = True
                print(f"Task '{todo_list[num - 1]['task']}' marked as completed.")
            else:
                print("Invalid task number!")

   
    elif choice == "3":
        if len(todo_list) == 0:
            print("To-do list is empty.")
        else:
            print("\nAll Tasks:")
            for i, t in enumerate(todo_list, 1):
                status = "Completed" if t["completed"] else "Pending"
                print(f"{i}. {t['task']} - {status}")

    
    elif choice== "4":
        completed_tasks = [t for t in todo_list if t["completed"]]
        if not completed_tasks:
            print("No completed tasks.")
        else:
            print("\nCompleted Tasks:")
            for i, t in enumerate(completed_tasks, 1):
                print(f"{i}. {t['task']}")

    
    elif choice== "5":
        pending_tasks = [t for t in todo_list if not t["completed"]]
        if not pending_tasks:
            print("No pending tasks.")
        else:
            print("\nPending Tasks:")
            for i, t in enumerate(pending_tasks, 1):
                print(f"{i}. {t['task']}")

    
    elif choice== "6":
        confirm = input("Are you sure you want to delete the entire list? (yes/no): ")
        if confirm.lower() == "yes":
            todo_list.clear()
            print("Entire to-do list deleted.")
        else:
            print("Action cancelled.")

    
    elif choice== "7":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 7.")
