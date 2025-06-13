#max numbers of three numbers
a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))

if a >= b and a >= c:
    print("Max is:", a)
elif b >= a and b >= c:
    print("Max is:", b)
else:
    print("Max is:", c)

#even or odd
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

number = int(input("Enter a number: "))
if is_even(number):
    print("Even")
else:
    print("Odd")





#divisible by 3 and 5
num = int(input("Enter number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by 3 and 5")
elif num % 3 == 0:
    print("Divisible by 3")
elif num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 3 or 5")