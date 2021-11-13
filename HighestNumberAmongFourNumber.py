a = int(input("Enter first number a: "))
b = int(input("Enter second number b: "))
c = int(input("Enter third number c: "))
d = int(input("Enter forth number d: "))

if a>b and a>c and a>d:
    print("A is the highest number.")
elif b>a and b>c and b>d:
    print("B is the highest number.")
elif c>a and c>b and c>d:
    print("C is the highest number.")
else:
    print("D is the highest number.")