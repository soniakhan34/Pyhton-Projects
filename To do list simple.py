# Simple To-Do List in Python

todo_list = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task to add: ")
        todo_list.append(task)
        print(f"Task '{task}' added successfully!")

    elif choice == "2":
        if not todo_list:
            print("Your to-do list is empty.")
        else:
            print("\nYour Tasks:")
            for idx, task in enumerate(todo_list, start=1):
                print(f"{idx}. {task}")

    elif choice == "3":
        if not todo_list:
            print("Your to-do list is empty. Nothing to remove.")
        else:
            print("\nTasks:")
            for idx, task in enumerate(todo_list, start=1):
                print(f"{idx}. {task}")
            try:
                task_num = int(input("Enter the task number to remove: "))
                if 1 <= task_num <= len(todo_list):
                    removed_task = todo_list.pop(task_num - 1)
                    print(f"Task '{removed_task}' removed successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
