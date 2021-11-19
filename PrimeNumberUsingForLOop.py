num = int(input("Enter a number: "))
flag = False
a=2
if num>a:
    for i in range(2, num):
        if num % i==0:
            flag = True
else:
    flag == True

if flag == False:
    print("Its a prime number.")
elif flag == True:
    print("Its not a prime number.")