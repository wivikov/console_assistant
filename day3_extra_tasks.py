num = int(input("Enter your number:"))
i = 1

while i <= 10 :
    print(f"{num} x {i} = {num * i}")
    i += 1

#Завдання 3 — Унікальні покупки
orders = set(["apple", "banana", "apple", "cherry", "banana"])
print(orders)

numbers = [5, 10, 3, 8]
print("Total:", sum(numbers))

scores = {
    "Max": 70,
    "Lena": 85,
    "Dima": 92,
    "Sofia": 78
}
print("Student with score more than 80:")
for student, score in scores.items():
    if score > 80:
        print(f"{student},{score}")

average_score = sum(scores.values()) / len(scores)
print(f"\nAvarage score: {average_score:.2f}")

for num in range(1, 6):
    print(f"\nТаблиця для {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

def multiply(a, b):
    return a * b
print(multiply(2,4))

def is_even(n):
     return n % 2 == 0
n = int(input("Number:"))
if is_even(n):
    print(" even")
else:
    print("odd")

def safe_divide(a,b):
    try:
        if isinstance(b, str):
            return "Incorrect type: b is a string"
        if b == 0:
            return "Can't divide by zero"
        return a / b
    except Exception as e:
        return f"Error: {e}"
print(safe_divide(4 , 2))
print(safe_divide(10 , 0))
print(safe_divide(5, "hi"))

def greet(name="Guest"):
    if name.capitalize() == "Admin":
        return "Welcome back, Admin, Full access"
    elif name.capitalize() == "Guest":
        return  f"Hello, {name}! Read only"
    else:
        return "No access"

