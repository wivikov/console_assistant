age = int(input("Enter your age:"))
if age >= 18:
    print("Дорослий")
elif age >= 13:
    print("Підліток")
else:
    print("Дитина")


num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
operation = input("Enter your operation,+,-,/,*")

if operation == "+":
    result = num1 + num2
    print("result:", result)
elif operation == "-":
    result = num1 - num2
    print("result:", result)
elif operation == "*":
    result = num1 * num2
    print("result:", result)
elif operation == "/":
    if num2 == 0:
        print("cant divide by  zero")
    else:
        result = num1 / num2
        print("result:", result)
else:
    print("Unknown operation.")

login = input("Enter your login:")
age_www = int(input("Please enter your age:"))
rules_www = input("Do you keep our rules yes/no").strip().lower()

if age_www >= 18 and rules_www == "yes":
    print(f"Access granted. Welcome, {login}!")
elif age_www >= 18 and rules_www != "yes":
    print("Access denied: you must be at least 18 years old.")
elif age_www <= 18:
    print("Access denied: you must be at 18 years old.")


