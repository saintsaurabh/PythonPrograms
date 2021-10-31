x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))


temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
