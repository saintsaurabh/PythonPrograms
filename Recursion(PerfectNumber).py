# Perfect number using Recursion
def perfect(num, res=0, i=1):
    if num <= i:
        return res

    elif num % i == 0:
        res += i
        if num == res:
            return res

    return perfect(num, res, i+1)


num1 = int(input("Enter the number: "))

if num1 == perfect(num1):
    print(num1, "is Perfect Number.")
else:
    print(num1, "is not Perfect Number.")
