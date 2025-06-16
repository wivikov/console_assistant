name = input("Enter you name:")
city = input("Enter you city:")
age = input("Enter you age:")
print(f"Hello, {name}! You are from {city} and you are {age} years old.")

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

user_data = {
"height": 1.82,
"is_student": False,
"nickname": "Bodik",
}
print(type(user_data["height"]))
print(type(user_data["is_student"]))
print(type(user_data["nickname"]))

