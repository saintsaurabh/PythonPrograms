var = [1, 3, "Ram", "Kam", "jama", 6, (6 + 9j), "Suraj", (1, 3, 4)]
lst = []
count1 = 0
count2 = 0
for i in var:
    if type(i) == str :
        count1 += 1
    elif type(i) in (int, bool, complex, float, tuple):
        count2 += 1
print(count1, count2)
