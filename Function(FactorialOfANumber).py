def factorial(args):

    fact = 1

    for i in range(1, args + 1):
        fact = fact * i

    return fact


res = factorial(int(input("Enter the number: ")))

print(res)
