def maximum(a, b, c):
    if a >=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

x = int(input("Enter first number:"))
y = int(input("Enter first number:"))
z = int(input("Enter third number:"))
print("maximum is:", maximum(x, y, z))

def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return  count
nums = [1,2,3,4,5,6,7,8,9,0]
print("Number of even number:", count_even(nums))