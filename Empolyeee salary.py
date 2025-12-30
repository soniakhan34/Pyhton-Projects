class Employee:
    def __init__(self,name, emp_id, salary):
        self.name = name          #public
        self.emp_id = emp_id      #public
        self.__salary = salary    #private

    def get_salary(self):
        return self.__salary

    def increment_salary(self,amount):
        if amount > 0:
            self.__salary +=amount
            print("Salary incremented successfully....")

        else:
            print("Invalid amount......")
        
    def display_employee(self):
        print('Employee Details')
        print('Name:',self.name)
        print('Employee id:', self.emp_id)




#=============== And Now the main Program ==============
print('..................Employee Salary System..................')

name=input('Enter the Employee Name: ')
emp_id=input('Enter employee ID: ')
salary=float(input('Enter salary: '))


emp = Employee(name, emp_id, salary)

while True:
    print("\n..................Menu...................")
    print("1. View Employee Info")
    print("2. View Salary")
    print("3. Increment Salary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp.display_employee()


    elif choice == "2":
        print("Current Salary:", emp.get_salary())


    elif choice == "3":
        amount = float(input("Enter increment amount: "))
        emp.increment_salary(amount)


    elif choice == "4":
        print("Thank you for using the Employee Salary System.")
        print("Made by Sonia..........")
        break


    else:
        print("Invalid choice! Please try again.")
