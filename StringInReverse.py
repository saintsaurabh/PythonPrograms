# Program to print string in reverse order
var = "python is easy"

res = []
temp = ''
for i in var:
    if i == ' ':
        res += [temp]
        temp = ''
    else:
        temp = i + temp
if temp:
    res += [temp]
print(res)
