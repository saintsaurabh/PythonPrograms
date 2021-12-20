def factors(args):

    print("The factors of", args, "are")

    for i in range(1, args):

        if args % i == 0:

            print(i, end=" ")


factors(int(input("Enter the number: ")))
