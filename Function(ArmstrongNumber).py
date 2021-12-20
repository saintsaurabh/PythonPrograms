def armstrong(args):
    temp = args
    res = 0
    while args > 0:
        digit = args % 10
        res += digit ** 3
        args = args // 10

    if temp == res:
        print("Its a armstrong")
    else:
        print("Its not a armstrong")


armstrong(int(input("Enter the number: ")))
