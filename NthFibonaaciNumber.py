num = int(input("Enter a nth place: "))
num1 = 0
num2 = 1
count = 1
for i in range(num-1):
    z = num1 + num2
    num1 = num2
    num2 = z
    count += 1
    if count == num:
        print(num1,"is the",num,"th fibonaaci number.")
        break


