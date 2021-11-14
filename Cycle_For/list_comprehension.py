# генераторы списков
# шабло [выражение for val in коллекция
a = [i for i in range(7)]
print(a)
a = [i ** 2 for i in range(1, 15)]
print(a)
a = [i % 4 for i in range(1, 15)]
print(a)
a = [i for i in 'hello']
import os
pppp = os.getpid()
print(a)
# шабло [выражение for val in коллекция if условие]
b = [elem for elem in a if elem % 2 == 0 and elem]
print(b)

a = input().split()
a = [int(i)for i in a]
print(a)

n = 5
m = 4
a = [[0] * m for i in range(n)]
for i in a:
    print(i)

a = [(i, j)for i in 'abc' for j in [1, 2, 3]]
print(a)

a = [i * j for i in [2, 3, 4, 5] for j in [1, 2, 3] if i * j >= 10]
print(a)
# При помощи генератора-списка сохраните в переменной zeroes список из 100 нулей.
# Выводить ничего не нужно, только правильно заполните список в переменной zeroes
zeroes = [[0] * 100 for i in range(100)]
# При помощи генератора-списка создайте список [1, 2, 3, ..., n],
# само натуральное число n будет поступать на вход вашей программе.
# В качестве ответа просто выведите получившийся список
n = int(input())
n = [int(i) for i in range(1, n + 1)]
print(n)
# При помощи list comprehension создайте список, состоящий из первых n заглавных букв английского алфавита
# ['A', 'B', 'C', 'D', ...]. Получить все заглавные буквы английского алфавита можно следующим образом:
# from string import ascii_uppercase
# print(ascii_uppercase) # выведет строку ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Входные данные
# На вход программе подается натуральное число n, n≤26.
# Формат выходных данных
# Программа должна вывести список из первых n заглавных букв английского алфавита
import string
from string import ascii_uppercase
n = int(input())
a = [string.ascii_uppercase[i] for i in range(n)]
print(a)
# Создайте список первых букв каждого слова из строки st и выведите его на экран
st = 'Create a list of the first letters of every word in this string'
a = st.split()
b = [i[0] for i in a]
print(b)
# Давайте усовершенствуем предыдущую задачу так, чтобы получался следующий список букв:
# ['A', 'BB', 'CCC', 'DDDD', 'EEEEE', 'FFFFFF', ...]
# Входные данные
# На вход программе подается натуральное число n, n ≤ 26.
# Формат выходных данных
# Программа должна вывести список из первых n заглавных букв английского алфавита,
# причем каждая буква должна быть продублирована в зависимости от своего порядкового номера
import string
from string import ascii_uppercase

n = int(input())
a = [string.ascii_uppercase[i] * (i + 1) for i in range(n)]
print(a)
# Программа принимает на вход два целых числа a и b.
# Если a<=b необходимо сформировать список квадратов целых чисел на интервале
# от а до b включительно и вывести его на экран.
# Если же a>b, необходимо сформировать список кубов целых чисел на интервале от a до b включительно,
# двигаясь в порядке убывания, и затем вывести его.
# Не забывайте пользоваться генератором списков
a, b = map(int, input().split())
print([i ** 2 for i in range(a, b + 1)] if a <= b else [i ** 3 for i in range(a, b -1, -1)])
# На вход программе подается натуральное число n (n<=1000).
# При помощи list comprehension создайте список, состоящий из делителей введенного числа.
n = int(input())
print([i for i in range(1, n + 1) if n % i == 0])
# более сложное
import random

a = [
    ('sidorov', 1995),
    ('lukov', 2002),
    ('petrov', 1991),
    ('garbachev', 1984),
    ('kostin', 2000),
    ('isaev', 2005),
    ('elisev', 1999),
    ('kozlov', 2004),
    ('bukov', 1995),
    ('gavrilov', 1989),
    ('efremov', 2006)
]
b = [elem[0] for elem in a if elem[0].startswith('e')]
print(b)

s = 'fjehwbfbh32hb3b2b3bkbkfbkb3'
b = [i for i in s if i.isdigit()]
print(b)
# что бы превратить полученные значение в списке в целые числа нужно:
s = 'fjehwbfbh32hb3b2b3bkbkfbkb3'
b = [int(i) for i in s if i.isdigit()]
print(b)

import random

n = 5
m = 3
a = [[random.randint(1, 6) for j in range(m)] for i in range(n)]
for i in a:
    print(i)

n = 7
m = 7
a = [[random.randint(1, 6) for j in range(m)] for i in range(n)]
for i in a:
    print(i)
b = [a[i][j] for i in range(n) for j in range(m) if
     i == j]  # берём только те элементы которые лежат на главной диаганали
c = [a[2][j] for j in range(m)]  # сохроняем только те элементы которые принадлежат второй строке
d = [a[i][3] for i in range(n)]  # берём элементы только одного столбца
print('main diagon', b)
print('2 stroka', c)
print('3 столбец', d)
# таблица умножений при помощи сложенный генераторов
n = 5
m = 5
a = [i * j for j in range(1, m + 1) for i in range(1, n + 1)]
for i in a:
    print(i)
# задача
# В вашем распоряжении есть двумерный список vector.
# Ваша задача при помощи генератора-списка сделать на основании vector линейный(одномерный ) список и вывести его
import itertools

vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

lst = [[1, 2, 3], [4], [5, 6, 7]]
print(list(itertools.chain.from_iterable(vector)))

vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
print([vector[i][j] for i in range(len(vector)) for j in range(len(vector[i]))])