# n = int (input("Введите цифру"))
# s = str()
# c = str()
# x = str()
# for i in range (0, n):
#     for l in range (1, n - i):
#         c += ' '

#     for j in range (n - i, n):
#         s += '*'

#     for l in range(n, n + i + 1):
#         x += '*'
#     print (f'{c}{s}{x}')
#     c = ''
#     s = ''
#     x = ''
# n = int (input())
# s = str()
# c = str()
# x = str()
# for i in range (0, n):
#     for l in range (1, n - i):
#         c += ' '

#     for j in range (n - i, n):
#         s += '*'

#     for l in range(n, n + i):
#         x += '*'
#     print (f'{c}{s}{x}')
#     c = ''
#     s = ''
#     x = ''
from random import randint

m = int (input('Введите M : '))
n = int (input('Введите N : '))

a = [[randint(1, 10) for j in range(m)] for i in range(n)]

print ('Сохранить файл? : ')
t = str(input('1) Да 0) Нет : '))
if t == '1':
    s = str(input('Введите название файла : '))
    open_file = open(f'/home/username/Рабочий стол/{s}.csv', 'w')
    open_file.write(f'{a}')
else:
    print (a)