# 1: Simple Number Triangle Pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

rows = int(input("Enter the number of rows: "))

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(i, end=' ')
    print()