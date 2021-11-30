# O/P :- {'a':5, 'b': 4, 'c':1, 'd':3}
# O/P :- {'a': 25, 'b': 16, 'c':1, 'd':9}
# O/P :- {'A': 25, 'B': 16, 'C':1, 'D':9}
z = "aaabbabcddadb"
count1, count2, count3, count4 = 0, 0, 0, 0
d = {}
for i in z:
    if i == 'a':
        count1 += 1
        d[i] = count1
    elif i == 'b':
        count2 += 1
        d[i] = count2
    elif i == 'c':
        count3 += 1
        d[i] = count3
    elif i == 'd':
        count4 += 1
        d[i] = count4
print(d)
s_d = {}
for j in d:
    s_d[j] = d[j]**2
print(s_d)
c_d = {}
for k in s_d:
    p = (chr(ord(k)-32))
    c_d[p] = s_d[k]
print(c_d)
