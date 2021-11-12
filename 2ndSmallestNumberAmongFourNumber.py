a = int(input("Enter first number a: "))
b = int(input("Enter second number b: "))
c = int(input("Enter third number c: "))
d = int(input("Enter fourth number d: "))

if a<b and a<c and a<d:
    if b<c:
        if b<d:
            print("B is 2nd smallest.")
        else:
            print("D is 2nd smallest.")
    else:
        if c<d:
            print("C is 2nd smallest.")
        else:
            print("D is 2nd smallest.")
if b<a and b<c and b<d:
    if a<c:
        if a<d:
            print("A is 2nd smallest.")
        else:
            print("D is 2nd smallest.")
    else:
        if c<d:
            print("C is 2nd smallest.")
        else:
            print("D is 2nd smallest.")
if d<a and d<b and d<c:
    if a<b:
        if a<c:
            print("A is 2nd smallest.")
        else:
            print("C is 2nd smallest.")
    else:
        if b<c:
            print("B is 2nd smallest.")
        else:
            print("C is 2nd smallest.")