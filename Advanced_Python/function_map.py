# 10.3 Функция map Python
# class map(object)
#   map(fuc, *iterables) --> map object
# map object - представляет собой итератор который вычисляет результат работы функции которую вы передали
# на каждый аргумент из этой последовательности

a = [-1, 2, -3, 4, 5]
b = list(map(abs, a))  # вворачиваем в вызов функции list
print(b)  # <map object at 0x7f431d2a5fa0>
# другой способ написания этой программы
c = [abs(i) for i in a]
print(c)  # [1, 2, 3, 4, 5]


# так же мы можем передавать функции которые сами создали

def f(x):
    return x ** 2


t = [-1, 2, -3, 4, 5]
e = list(map(f, t))  # передали нашу созданную функцию f
print(e)  # [1, 4, 9, 16, 25]
# пример со строками
s = ['hello', 'hi', 'helloworld']
n = list(map(len, s))
print(n)  # [5, 2, 10]
# в качестве функции мы можем передавать не только встроенные и самописные функции но и методы этих объектов
s = ['hello', 'hi', 'helloworld']
n = list(map(str.upper, s))
print(n)  # ['HELLO', 'HI', 'HELLOWORLD']
# так же в функцию мап можно передавать анонимную функцию
s = ['hello', 'hi', 'helloworld']
n = list(map(lambda x: x[::-1], s))
print(n)  # ['olleh', 'ih', 'dlrowolleh']
o = list(map(lambda x: x + '!', s))
print(o)  # ['hello!', 'hi!', 'helloworld!']
# так же можно строку переобразовать в список
p = list(map(list, s))
print(p)  # [['h', 'e', 'l', 'l', 'o'], ['h', 'i'], ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']]
m = list(map(sorted, p))  # сортируем список p
print(m)

k = map(int, input().split())  # что вводить неопределённое количества чисел через пробел
print(k)
# задачка
# Напишите программу, которая возводит в квадрат и в куб каждое число из списка numbers
# пользуясь при этом функциями map и lambda.
# В результате у вас должно получится два отдельных списка: в одном квадраты,
# в другом кубы. Их необходимо вывести на экран.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = list(map(lambda x: x ** 2, numbers))
m = list(map(lambda x: x ** 3, numbers))
print(n, m, sep='\n')