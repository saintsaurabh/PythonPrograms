num = int(input("Enter the number: "))
num1 = 0
num2 = 1
count = 0
for i in range(num):
    z = num1 + num2
    num1 = num2
    num2 = z
    count += 1
    if count == num:
        print(num1,"is the",num,"fibonaaci series.")
        break