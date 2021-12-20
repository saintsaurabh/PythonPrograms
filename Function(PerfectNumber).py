def perfect(args):

    res = 0

    for i in range(1, args):
        if args % i == 0:
            res += i

    if res == args:
        print("Its a perfect number.")
    else:
        print("Its not a perfect number.")


perfect(int(input("Enter the number: ")))
