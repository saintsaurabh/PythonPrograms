def even(*args):

    res = []

    for i in args:

        if i % 2 == 0:

            res += [i]

    return res


output = even(12, 13, 14, 15, 16, 17, 89, 90, 234, 3989, 98765, 123453, 456, 132124, 19, 298, 243)

print(output)

