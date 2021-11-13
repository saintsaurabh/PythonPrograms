num = int(input("Enter the number: "))

print("\nFactors of ",num," is:- ")
i = 1
while i <= num:
    if num % i == 0:
        print(i)
    i += 1
