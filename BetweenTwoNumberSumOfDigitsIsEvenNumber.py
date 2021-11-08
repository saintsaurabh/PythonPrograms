for i in range(1, 100):
    num = i
    sum = 0
    while(num != 0):
        digit = num % 10
        sum = sum + digit
        num = num // 10
    if(sum%2 == 0):
        print(i)