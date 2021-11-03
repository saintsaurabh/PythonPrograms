def UncommonWords(A, B):
    count = {}

    for word in A.split():
        count[word] = count.get(word, 0) + 1

    for word in B.split():
        count[word] = count.get(word, 0) + 1

    return [word for word in count if count[word] == 1]

A = input("Enter the first string:- ")
B = input("Enter the second string:- ")

print(UncommonWords(A, B))
