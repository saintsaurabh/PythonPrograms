# Two strings are said to be anagram if we can form one string by arranging the characters of another string.
str1 = str(input("Enter the first word:- "))
str2 = str(input("Enter the second word:-"))

str1 = str1.lower()
str2 = str2.lower()

if(len(str1) == len(str2)):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    if(sorted_str1 == sorted_str2):
        print(str1 + " and " + str2 + " are anagram.")
    else:
        print(str1 + " and " + str2 + " are not anagram.")

else:
    print(str1 + " and " + str2 + " are not anagram.")
