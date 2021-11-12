a = int(input("Enter first number a: "))
b = int(input("Enter second number b: "))
c = int(input("Enter third number c: "))
d = int(input("Enter forth number d: "))

if a>b and a>c and a>d:
    if b>c:
        if b>d:
            print("B is 2nd greatest number.")
        else:
            print("D is 2nd greatest number.")
    else:
        if c>d:
            print("C is the 2nd greatest.")
        else:
            print("D is the 2nd greatest.")
if c>a and c>b and c>d:
    if a>b:
        if a>d:
            print("A is the second greatest.")
        else:
            print("D is the second greatest.")
    else:
        if b>d:
            print("B is the second greatest.")
        else:
            print("D is the second greatest.")
if d>a and d>b and d>c:
    if a>b:
        if a>c:
            print("A is the second greatest.")
        else:
            print("C is the second greatest.")
    else:
        if b>c:
            print("B is the second greatest.")
        else:
            print("C is the second greatest.")