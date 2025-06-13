#calculator
try:
 #first number/second
    num1 = float(input("Ведди перше число:"))
    num2 = float(input("Ведди друге число:"))
    operation = input("Ведди операцію (*,+,-,/):")
 #operation
    if operation == "+":
        result = num1 + num2
        print("Результат", result)
    elif operation == "-":
        result = num1 - num2
        print("Результат:", result)
    elif operation == "*":
        result = num1 * num2
        print("Результат:", result)
    elif operation =="/":
        if num2 == 0:
            print("Помилка ділення на 0")
        else:
            result = num1 / num2
            print("Результат:", result)
    else:
        print("Невідома операція:")
     #except
except ValueError:
    print("Будь ласка , введи число коректно")