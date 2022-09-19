numbers = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4]


def Sort(number):
    Sort_Numbers = []
    num = number[0]
    Sort_Numbers.append(num)
    for i in number:
        if i == num:
            continue
        else:
            num = i
            Sort_Numbers.append(i)

    return Sort_Numbers


print(Sort(numbers))
