str = input("Enter a string: ")

lst = []
for i in range(len(str)):
    if 'a' <= str[i] <= 'z' or 'A' <= str[i] <= 'Z':
        if str[i] in 'aeiouAEIOU':
            lst = lst + [i**3]
print(lst)
