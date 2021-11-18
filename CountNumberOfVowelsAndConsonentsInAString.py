str = input("Enter a string: ")

vow = []
cons = []
i = 0
while i <len(str):
    if 'a'<= str[i] <='z' or 'A'<= str[i] <='B':
        if str[i] in 'aeiouAEIOU':
            vow += [str[i]]
        else:
            cons += [str[i]]
    i += 1
print("Vowels in the given string are :",vow)
print("Consonents in the given string are: ",cons)
print("Length of Vowels are: ",len(vow))
print("Length of Consonents are: ",len(cons))