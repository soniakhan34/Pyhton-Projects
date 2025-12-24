#--------------------------To Do list Application Project-----------------------
#Create Main file--------------
# file name..........(main file.py)

from file1 import (add_task, show_tasks, delete_task)
from file2 import (save, load)

tasks =[]
print("\n----------------Now start the To-do-List Application Project------------------")
while True:
    print('1)====================(Add the Tasks)============================')
    print('2)====================(View the Tasks)===========================')
    print('3)====================(Delete the Task)==========================')
    print('4)====================(Save the Task)============================')
    print('5)====================(Load the Task)============================')
    print('6)====================(Exit the Task)===========================')

    choice=input("Enter the choice---------: ")

    if choice =='1':
        title = input("Enter the task name: ")
        add_task(tasks, title)

    elif choice =='2':
        show_tasks(tasks)

    elif choice =='3':
        show_tasks(tasks)
        num = int(input("Enter the task number: "))-1
        delete_task(tasks, num)

    elif choice =='4':
        save(tasks)

    elif choice =='5':
        tasks = load()

    elif choice =='6':
        print("Closed the Program................")
        print("Thank you for using my project.......Sonia.........")
        break

    else:
        print("Wrong choice!!!!!!!!!!")
