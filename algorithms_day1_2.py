#* numbers
num = int(input("Enter a number:"))
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")


#sum numbers 1 to N
n = int(input("enter first number:"))
total = 0

for i in range(1, n+1):
    total += i
print("Sum from 1 to", n, "is:", total)

#checking for prime number
nums = int(input("Enter number:"))
is_prime = True
if nums < 2:
    is_prime=False
else:
    for i in range(2, int(nums**0.5)+1):
        if nums % i == 0:
            is_prime = False
            break
if is_prime:
    print("Prime")
else:
    print("Not prime")