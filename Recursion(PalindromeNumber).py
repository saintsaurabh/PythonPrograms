# Palindrome number using Recursion
def pal(num, res=0):
    if num <= 0:
        return res
    rem = num % 10
    res = res*10 + rem
    num //= 10
    return pal(num, res)


num=int(input("Enter the number: "))

if num == pal(num):
    print("Palindrome")
else:
    print("Not palindrome")
