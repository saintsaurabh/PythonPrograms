num = int(input("Enter a number: "))
num1 = 0
num2 = 1
for i in range(num-1):
    if num1 <= num:
        if num == num1:
            print("Its a Fibonaaci number.")
            break
        z = num1 + num2
        num1 = num2
        num2 = z
    else:
        print("Its not a Fibonaaci number.")
        break


