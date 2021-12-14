# 8: Pyramid of Natural Numbers Less Than 10
# Pattern:

# 1

# 2 3 4

# 5 6 7 8 9
num = 1

stop = 2

rows = int(input("Enter the number of rows: "))

for i in range(1, rows+1):

    for j in range(1, stop):

        print(num, end=" ")

        num += 1

    print("\n")

    stop += 2