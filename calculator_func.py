def calculate(a , b ,operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "Cannot divide by zero:"
        return a / b
    else:
        return "Unknown operation"

while True:
    try:
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))
        op = input("Choose operation(+, -, *, /,):")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue

    result = calculate(num1, num2, op)
    print("Result:", result)

    choice = input("Do you want co countinue?  (yes/no):").lower()
    if choice != "yes":
        print("Goodbye!")
        break        