# Strong number using Recursion
def factorial(var):
    if var <= 0:
        return 1
    return var * factorial(var - 1)


def strong(num, res=0):
    if num <= 0:
        return res
    fact = 1
    digit = num % 10
    fact = factorial(digit)
    res += fact
    num //= 10

    return strong(num, res)


num = int(input("Enter the number: "))

if num == strong(num):
    print(num, "is Strong Number.")
else:
    print(num, "is not Strong Number.")
