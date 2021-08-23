# Метод подсчёта. Сортировка подсчётом Python
a = [0, 1, 2, 3, 2, 4, 5, 2, 4, 1, 3, 4, 4]
count = [0] * 6
for i in a:
    count[i] += 1
print(count)
for i in range(6):
    if count[i] > 0:
        print((str(i) + ' ') * count[i], end='')

s  = "fhhf  FH hjfjjf frfef 4564 *)(#))$*)"
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

