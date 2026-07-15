print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {result}")

elif choice == "2":
    result = num1 - num2
    print(f"The result of {num1} - {num2} is: {result}")

elif choice == "3":
    result = num1 * num2
    print(f"The result of {num1} * {num2} is: {result}")

elif choice == "4":
    # Check for division by zero to prevent a runtime error
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")

else:
    print("Invalid choice! Please run the program again and select a number from 1 to 4.")
