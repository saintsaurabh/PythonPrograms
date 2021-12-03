num = int(input("Enter the number: "))

temp = num
res = 0
while num > 0:
    rem = num % 10
    fact = 1
    for i in range(1, rem + 1):
        fact = fact * i
    res = res + fact
    num = num // 10
if temp == res:
    print("Strong number.")
else:
    print("Not a prime number.")
