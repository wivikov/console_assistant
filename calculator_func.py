def calculate(a , b ,operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return ("Cannot divide by zero:")
        return a / b
    else:
        return "Unknown operation"

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second numbr:"))
op = input("chose operation (+, -, *, /): ")

result = calculate(num1, num2, op)
print("Result:", result)
