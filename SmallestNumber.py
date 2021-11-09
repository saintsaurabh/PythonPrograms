a = int(input("Enter first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a < b and b < c:
    print("A is smallest number.")
elif b < a and a < c:
    print("B is the smallest number.")
elif c < a and c < b:
    print("C is the smallest number.")
else:
    print("Invalid input.")