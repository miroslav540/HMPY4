def Search_Numbers(num):
    Simple_Factor = []
    i = 2
    while num > 1:
        if num % i == 0:
            Simple_Factor.append(i)
            while num % i == 0:
                num /= i
        else:
            i += 1
    return Simple_Factor


num = Search_Numbers(int(input('Enter the number -> ')))
print(num)
