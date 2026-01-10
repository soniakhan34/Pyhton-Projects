from datetime import datetime

class Task:
    task_no = 1

    def __init__(self, title, due_date, priority, category):
        self.id = Task.task_no
        Task.task_no += 1

        self.title = title
        self.due_date = due_date
        self.priority = priority
        self.category = category
        self.status = "Pending"
        self.created_on = datetime.now()

    def complete(self):
        self.status = "Completed"

    def overdue(self):
        if self.status == "Pending" and datetime.now().date() > self.due_date:
            return True
        return False



class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        for t in self.tasks:
            print(f"{t.id}. {t.title} | {t.priority} | {t.status} | {t.due_date}")

    def complete_task(self, task_id):
        for t in self.tasks:
            if t.id == task_id:
                t.complete()
                print("Task completed!")
                return
        print("Task not found.")

    def show_pending(self):
        for t in self.tasks:
            if t.status == "Pending":
                print(f"{t.id}. {t.title}")

    def show_overdue(self):
        for t in self.tasks:
            if t.overdue():
                print(f"{t.id}. {t.title} (Overdue)")


# ---------------- MAIN PROGRAM ----------------
todo = TaskList()

while True:
    print("\n----------- TO DO LIST --------------")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. View Pending Tasks")
    print("4. Complete Task")
    print("5. View Overdue Tasks")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Task title: ")
        date_input = input("Due date: ")
        due_date = datetime.strptime(date_input, "%Y-%m-%d").date()
        priority = input("Priority (High/--Medium/---Low): ")
        category = input("Category: ")

        task = Task(title, due_date, priority, category)
        todo.add_task(task)
        print("Task added successfully.....!")

    elif choice == "2":
        todo.show_tasks()

    elif choice == "3":
        todo.show_pending()

    elif choice == "4":
        tid = int(input("Enter task number: "))
        todo.complete_task(tid)

    elif choice == "5":
        todo.show_overdue()

    elif choice == "6":
        print("Program closed.")
        break

    else:
        print("Wrong choice!")
