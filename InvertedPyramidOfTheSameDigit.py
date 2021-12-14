# 5: Inverted Pyramid of the Same Digit
# Pattern:

# 5 5 5 5 5

# 5 5 5 5

# 5 5 5

# 5 5

# 5
rows = int(input("Enter the number: "))
num = int(input("Enter the digit: "))
for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print(num, end=" ")
    print('\n')