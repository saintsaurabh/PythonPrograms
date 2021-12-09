list1 = ["google.com", "facebook.com", "olx.in", "amazon.com", "youtube.com", "netflix.com", "instagram.com"]
list2 = []

reqDict = {}
for word in list1:
    res = ''
    for alpha in word:
        if alpha != ".":
            res += alpha
        else:
            list2 += [res]
            res = ''
    list2 += [res]
for k in range(len(list2)):
    if len(list2) % 2 == 0:
        if k % 2 == 0:
            reqDict[list2[k]] = list2[k+1]

print(reqDict)
