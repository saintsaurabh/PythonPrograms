# 407 = 4*4*4 + 0*0*0 + 7*7*7
num = int(input("Enter a number: "))

sum = 0

cool = num
while cool > 0:
    digit = cool % 10
    sum += digit ** 3
    cool //= 10

if num == sum:
    print(num," is an Armstrong number.")
else:
    print(num," is not an Armstrong number.")