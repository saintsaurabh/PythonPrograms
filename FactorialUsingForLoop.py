num = int(input("Enter the number: "))

fact = 1
if num >= 0:
    for i in range(1, num+1):
        fact = fact * i
    print("Factorial of",num,"is", fact)
else:
    print("Invalid input.")