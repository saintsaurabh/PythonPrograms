def add(n1, n2):

    return n1+n2


def sub(n1, n2):

    return n1-n2


def multi(n1, n2):

    return n1*n2


def div(n1, n2):

    return n1//n2


def get_data():
    start = int(input("Enter the first number: "))
    end = int(input("Enter the second number: "))
    return start, end


while True:

    print("Press 1 for addition.")
    print("Press 2 for subtraction.")
    print("Press 3 for multiplication.")
    print("Press 4 for division.")
    print("Press 5 for stop.")
    choice = int(input("Enter any of the choice given above: "))

    if choice == 1:
        data = get_data()
        print(add(*data))

    elif choice == 2:
        data = get_data()
        print(sub(*data))

    elif choice == 3:
        data = get_data()
        print(multi(*data))

    elif choice == 4:
        data = get_data()
        print(div(*data))

    elif choice == 5:
        break

    else:
        print("InValid input choice.")
