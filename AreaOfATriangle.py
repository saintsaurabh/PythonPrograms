a = int(input("Enter the 1st Dimension:- "))
b = int(input("Enter the 2nd Dimension:- "))
c = int(input("Enter the 3rd Dimension:- "))

s = (a + b + c) / 2

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' % area)