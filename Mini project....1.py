while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ")

        if operator == "+":
            print("Result:", num1 + num2)

        elif operator == "-":
            print("Result:", num1 - num2)

        elif operator == "*":
            print("Result:", num1 * num2)

        elif operator == "/":
            print("Result:", num1 / num2)

        else:
            print("Invalid operator. Please use +, -, *, or /.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    choice = input("Do you want to continue? (yes/no): ").lower()
    if choice != "yes":
        print("Program ended.")
        break
