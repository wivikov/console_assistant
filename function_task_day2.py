def is_even(num):
    return num % 2 == 0
number = int(input("Enter a number:"))
if is_even(number):
    print("Even")
else:
    print("Odd")

def factorial(n):
    if n == 0 :
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a number for factorial:"))
print(f"Factorial of {num} is {factorial(num)}")
