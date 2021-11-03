def remove(string, i):
    for j in range(len(string)):
        if j == i:
            string = string.replace(string[i], "", 1)
    return string

if __name__ == '__main__':
    string = input("Enter a string:- ")

    i = int(input("Enter the i-th element:- "))

    print(remove(string, i))
