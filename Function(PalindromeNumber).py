def palindrome(args):

    num = args
    rev = 0

    while args > 0:

        res = args % 10
        rev = rev * 10 + res
        args = args // 10

    if rev == num:

        print("Its a palindrome number.")
    else:

        print("Its not a palindrome number.")


palindrome(int(input("Enter the number: ")))
