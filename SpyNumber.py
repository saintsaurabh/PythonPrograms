# Spy number:- A spy number is a number where the sum of its digits equals the product of its digits.
r1 = int(input("Enter the first range: "))
r2 = int(input("Enter the second range: "))
for j in range(r1, r2+1):
    num = str(j)
    sum = 0
    mult = 1
    for i in num:
        sum = sum + int(i)
        mult = mult * int(i)
    if sum == mult:
        print(j)