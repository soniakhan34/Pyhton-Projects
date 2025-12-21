---
title: "My First Python Project"
datePublished: Sun Dec 21 2025 10:34:15 GMT+0000 (Coordinated Universal Time)
cuid: cmjflb2cu000602l27vcb4ror
slug: my-first-python-project
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1766312643750/a6dbbab6-3f99-4ac2-b384-73409516b1d1.png

---

def add(a, b): return a + b

def subtract(a, b): return a - b

def multiply(a, b): return a \* b

def divide(a, b): if b == 0: return "Error! Cannot divide by zero." return a / b

print("Welcome to the Simple Calculator!") print("Enter 'q' at any time to quit.\\n")

while True: num1 = input("Enter first number: ").casefold() if num1 == 'q':

print("Exiting calculator. Goodbye!") break num2 = input("Enter second number: ").casefold() if num2 == 'q':

print("Exiting calculator. Goodbye!") break operation = input("Enter operation (+, -, \*, /): ").casefold() if operation == 'q': print("Exiting calculator. Goodbye!")

break

try: num1 = float(num1) num2 = float(num2) except ValueError:

print("Invalid input! Please enter numeric values.\\n") continue

if operation == '+': print(f"Result: {add(num1, num2)}\\n") elif operation == '-':

print(f"Result: {subtract(num1, num2)}\\n") elif operation == '\*':

print(f"Result: {multiply(num1, num2)}\\n") elif operation == '/': print(f"Result: {divide(num1, num2)}\\n") else: print("Invalid operation! Please choose +, -, \*, or /.\\n")