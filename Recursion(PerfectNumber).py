# Perfect number using Recursion
def perfect(num, res=0, i=1):
    if num <= i:
        return res

    elif num % i == 0:
        res += i

    return perfect(num, res, i+1)


num = int(input("Enter the number: "))

if num == perfect(num):
    print(num, "is Perfect Number.")
else:
    print(num, "is not Perfect Number.")
