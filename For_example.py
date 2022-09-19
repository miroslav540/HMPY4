import os
os.system('CLS')

Students = {}
Students = \
    {
        'Ангела Меркель 5'
        'Андрей Валетов 5'
        'Фредди Меркури 3'
        'Анастасия Пономарева 4'
        'Константин Дьяволов 1'
    }

with open('For_example.txt', 'w', encoding='utf-8') as data:
    for i in Students:
        data.write(i + '\n')

    print(Students)

with open('For_example.txt', 'a', encoding='utf-8') as data:
    for student, mark in Students:
        n = 5
        if Students[student] == n:
            data.write('\n' + student.upper())
            x = student.upper()
            print(x)
        else:
            data.write('\n' + student + ' ' + str(mark))
