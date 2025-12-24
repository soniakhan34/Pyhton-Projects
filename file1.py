#--------------------------To Do list Application Project-----------------------
#Create file1--------------
# file name..........(file1.py)

def add_task(tasks, title):
    tasks.append({"title": title, "completed": False})


def show_tasks(tasks):

    if len(tasks) == 0:
        print("No tasks found")

    else:
        for i in range(len(tasks)):
            print(i + 1, tasks[i] ["title"])


def delete_task(tasks, num):

    if num < len(tasks):
        tasks.pop(num)
        print("Task are deleted...........")

    else:
        print("Wrong task number..........")
