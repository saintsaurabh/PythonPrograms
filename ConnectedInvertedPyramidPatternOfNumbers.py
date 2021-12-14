# 11: Connected Inverted Pyramid Pattern of Numbers
# Pattern:

# 5 4 3 2 1 1 2 3 4 5

# 5 4 3 2 2 3 4 5

# 5 4 3 3 4 5

# 5 4 4 5

# 5 5
rows = int(input("Enter the number of rows: "))
for i in range(1, rows+1):

    for j in range(rows, i-1, -1):
        print(j, end=" ")

    for j in range(i, rows+1):
        print(j, end=" ")

    print("\n")