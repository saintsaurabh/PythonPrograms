# WAP to print index number of vowels present in a string
num = input("Enter a string: ")

for i in range(len(num)):
    if 'a'<= num[i] <= 'z' or 'A' <= num[i] <= 'Z':
        if num[i] in 'aeiouAEIOU':
            print(i)