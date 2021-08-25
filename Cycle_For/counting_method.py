# Метод подсчёта. Сортировка подсчётом Python
a = [0, 1, 2, 3, 2, 4, 5, 2, 4, 1, 3, 4, 4]
count = [0] * 6
for i in a:
    count[i] += 1
print(count)
for i in range(6):
    if count[i] > 0:
        print((str(i) + ' ') * count[i], end='')

s = "fhhf  FH hjfjjf frfef 4564 *)(#))$*)"
letters = [0] * 26
for i in s.lower():
    if "a" >= i <= 'z':
        nomer = ord(i) - 97
        letters[nomer] += 1

for i in range(26):
    if letters[i] > 0:
        print(chr(i + 97) * letters[i], end='')

a = []
import random

for i in range(10):
    a.append((random.randint(-10, 10)))

count = [0] * 21
for i in a:
    count[i + 10] += 1
print(a)
for i in range(21):
    if count[i] > 0:
        print(i - 10, count[i])
# задачки
# Давайте на практике применим метод подсчета
# На вход вашей программе поступает положительное целое число n, а ваша задача вывести в порядке возрастания все
# цифры, которые встречались в этом числе, и напротив каждого также необходимо вывести сколько раз данная цифра
# встречалась в числе n
# вриант №1
n = input()
for i in range(10):
    if str(i) in n:
        print(i, n.count(str(i)))
# вриант №2
m = list(map(int, input()))
count = [0] * 10
for i in m:
    count[i] += 1
for i in range(10):
    if count[i] > 0:
        print(i, count[i])
# Сортировка подсчетом Как видно из названия задачи, вам необходимо отсортировать список, состоящий только из чисел в
# пределах от -100 до 100 включительно, сортировкой подсчетом. Программа получает на вход число n - количество
# элементов в списке, затем сами элементы списка
# Вам необходимо вывести отсортированный список
# P.S. не пользуйтесь встроенной функцией sorted или методом sort
n = int(input())
s = list(map(int, input().split()))
a = []
while len(s) != 0:
    a.append(min(s))
    s.remove(min(s))
for i in a:
    print(i, end=" ")

