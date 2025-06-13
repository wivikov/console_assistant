#парне не парне число
num = int(input("your number"))
if num % 2 == 0:
    print('Парне')
else:
    print('Непарне')

#вік
age = int(input("Вік:"))
if age >=18:
     print("Ви повнолітній")
else:
    print("Ви не повнолітній")

#виведеня 3 чисел
a = int(input("Перше число"))
b = int(input("Друге число"))
c = int(input("Третє число"))

if a >= b and a>=c:
    print("Найбільше:",a)
elif b>=a and b>=c:
    print("Найбільше:", b)
else:
    print("Найбільше:", c)

#пароль
password = input("Ведіть пароль:")

if password == "admin123":
    print("password correct:")
else:
    print("password incorrect:")
#веди число перевірка ділення на 3 5
cislo = int(input("Ведди число:"))

if num % 3 == 0 and num % 5 == 0:
    print("кратне на 3 і на 5 ")
else:
    print("Nt")

#calculator
try:
    num1 = float(input("Ведди перше число:"))
    num2 = float(input("Ведди друге число:"))
    operation = input("Ведди операцію (*,+,-,/):")
    if operation == "+":
        result = num1 + num2
        print("Результат", result)
    elif operation =="-":
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
except ValueError:
    print("Будь ласка , введи число коректно")