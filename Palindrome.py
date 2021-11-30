# A palindromic number is a number that remains the same when its digits are reversed.
num = int(input("Enter the number: "))
temp = num
rev = 0
while num>0:
    a = num % 10
    rev = rev * 10 + a
    num = num // 10
if temp == rev:
    print("Its a palindrom number.")
else:
    print("Its not a palindrom number.")