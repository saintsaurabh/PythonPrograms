# Prime number using Recursion
def prime(num, flag=None):
    if flag is None:
        flag = num - 1

    if flag >= 2:
        if num % flag == 0:
            print(num, "is not Prime Number.")
            return False
        return prime(num, flag - 1)
    else:
        print(num, "is Prime Number.")
        return True


num = int(input("Enter the number: "))

prime(num)
