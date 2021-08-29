# Вложенные списки
a = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, [3, 4, 5], 7, 19]]
print(a[2][2][1])

a = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, 17, 19]]
b = ['hell', 'hi', 'world']
print(b[2][0])
a = [
    [0, 2, 4, 6],
    [1, 5, 9, 13],
    [3, 10, 17, 19]
]
# первый вариант обхода списков (обход по значениям)
for i in a:
    for j in i:
        print(j, end=' ')
    print()
# обход по индексам
a = [
    [0, 2, 4, 6],
    [1, 5, 9, 13],
    [3, 10, 17, 19]
]
for i in range(3):
    for j in range(4):
        a[i][j] += 10
        print(a[i][j], end=' ')
    print()
print(a)
# при таком вариенте обхода можно менгять значение элементов
# обход по индексам в обратном порядке
a = [
    [0, 2, 4, 6],
    [1, 5, 9, 13],
    [3, 10, 17, 19]
]
for i in range(2, -1, -1):
    for j in range(3, -1, -1):
        a[i][j] += 10
        print(a[i][j], end=' ')
    print()
print(a)
#   нахождение суммы по строкам
for i in range(3):
    s = 0
    for j in range(4):
        s += a[i][j]
    print(s)
# нахождение суммы по столбцам
for j in range(4):
    s = 0
    for i in range(3):
        s += a[i][j]
    print(s)
    # обход по индексам в обратном порядке
    a = [
        [0, 2, 4, 6],
        [1, 5, 9, 13],
        [3, 10, 17, 19]
    ]
    for i in range(2, -1, -1):
        for j in range(3, -1, -1):
            a[i][j] += 10
            print(a[i][j], end=' ')
        print()
    print(a)
# заполнение вложенного списка
a = []
n = int(input())
m = int(input())
for i in range(n):
    a.append([0]*m)
for i in a:
    print(i)
# заполнение вложенного списка
a = []
n = int(input())
m = int(input())
for i in range(n):
    b = []
    for j in range(m):
        b.append(int(input()))
    a.append(b)
for i in a:
    print(i)

a = []
n = int(input())
for i in range(n):
    a.append([0] * n)
for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = 10
        elif i > j:
            a[i][j] = 3
        else:
            a[i][j] = 5
for i in a:
    print(i)
# задачки

