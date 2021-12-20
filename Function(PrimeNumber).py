def prime(args):
    flag = False

    for i in range(2, args):
        if args % i == 0:
            flag = True

    if flag is True:

        print("Its not a prime number.")

    elif flag is False:

        print("Its a prime number.")


prime(int(input("Enter the number: ")))
