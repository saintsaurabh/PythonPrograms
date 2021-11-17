num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
multiple = int(input("Enter the multiple: "))

for i in range(num1,num2):
    if i % multiple == 0:
        print(i)
