def calculator(a, b, operation):
    try:
        a = float(a)
        b = float(b)
        if operation == "+":
            return  a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            return a / b
        else:
            return "Unknown operation"
    except ZeroDivisionError:
        return "Cant divide by zero"
    except ValueError:
        return "Enter a valid number"
