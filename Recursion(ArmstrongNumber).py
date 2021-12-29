# Armstrong number using Recursion
def armstrong(num, res=0):
    if num <= 0:
        return res
    digit = num % 10
    res = res + digit**4
    num //= 10
    return armstrong(num, res)


num=int(input("Enter the number: "))

if num == armstrong(num):
    print(num,"is Armstrong Number.")
else:
    print(num,"is not Armstrong Number.")
