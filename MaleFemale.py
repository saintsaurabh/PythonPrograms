male = int(input("Enter the male age: "))
female = int(input("Enter the female age: "))

if male>=22 and not female >= 18:
    print("Male is eligible but female is not eligible.")
elif not male >= 22 and female >= 18:
    print("Female is eligible but male is not.")
elif male >= 22 and female >= 18:
    print("Both are eligible")
elif not male>=22 and not female>=18:
    print("Both are not eligible")


