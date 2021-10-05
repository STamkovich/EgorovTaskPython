# Функции.Определение и вызов
""" Функции - многократно используемые фрагменты программы. При помощи функции можно объеденить несколько инструкций
в один блок, присвоить этому блоку имя и затем, обращаясь по имени этого блока, выполнить инструкции внутри его
в любом месте программы необходимое число раз"""


# определение функции
def sayHello():
    print('hello')
    print('world')
    print('and everybody')


def square(x):
    print('Квадрат числа', x, '=', x ** 2)


sayHello()
square(5)

for i in range(1, 11):
    square(i)


def multiply(a, b):
    print(a * b)


# Напишите функцию check_password, которая проверяет переданный ей пароль на сложность
# и печатает на экран результат проверки.
# Сложным паролем будет считаться комбинация символов, в которой :
# Есть хотя бы 3 цифры
# Есть хотя бы одна заглавная буква
# Есть хотя бы один символ из следующего набора "!@#$%*"
# Общая длина не менее 10 символов
# Если пароль прошел все проверки, функция должна вывести на экран фразу "Perfect password",
# в противном случае - "Easy peasy"
# Вам необходимо написать только определение функции


def check_password(str):
    count = []
    count1 = []
    count2 = []

    for i in str:
        if i in '1,2,3,4,5,6,7,8,9,0':
            count.append(i)
        elif i in "!,@,#,$,%,*":
            count2.append(i)
        elif i == i.upper():
            count1.append(i)
    if len(count) >= 3 and len(count1) >= 1 and len(count2) >= 1 and len(str) >= 10:
        print("Perfect password")
    else:
        print("Easy peasy")


check_password('qwerty')

multiply(3, 5)


def even(a):
    if a % 2 == 0:
        print(a, 'chetnoe')
    else:
        print(a, 'nechetnoe')


even(5)


def factorial(n):
    pr = 1
    for cis in range(2, n + 1):
        pr = pr * cis
    print(pr)


factorial(4)

if 5 > 7:
    def primer():
        print('hello')
else:
    def primer():
        print('HELLO')

primer()


# задачки
# Напишите функцию summa_n,которая принимает одно целое положительное t
# число и находит сумму всех чисел от 1 до t включительно.
# Программа должна распечатать сообщение
# "Я знаю, что сумма чисел от 1 до {t} равна {S}",
# где в качестве t и S вам необходимо подставить значения (см. тестовые данные)
# Ваша задача написать только определение функции, вызывать ее не нужно

# Зачем нужны функции в программировании!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def summa_n(t):
    s = 0
    for i in range(1, t + 1):
        s = s + i
    print(f'Я знаю, что сумма чисел от 1 до {t} равна {s}')


summa_n(5)


# Напишите функцию check_password, которая проверяет переданный ей пароль на сложность
# и печатает на экран результат проверки.
# Сложным паролем будет считаться комбинация символов, в которой :
# Есть хотя бы 3 цифры
# Есть хотя бы одна заглавная буква
# Есть хотя бы один символ из следующего набора "!@#$%*"
# Общая длина не менее 10 символов
# Если пароль прошел все проверки, функция должна вывести на экран фразу "Perfect password",
# в противном случае - "Easy peasy"
# Вам необходимо написать только определение функции


def check_password(str):
    count = []
    count1 = []
    count2 = []

    for i in str:
        if i in '1,2,3,4,5,6,7,8,9,0':
            count.append(i)
        elif i in "!,@,#,$,%,*":
            count2.append(i)
        elif i == i.upper():
            count1.append(i)
    if len(count) >= 3 and len(count1) >= 1 and len(count2) >= 1 and len(str) >= 10:
        print("Perfect password")
    else:
        print("Easy peasy")


check_password('qwerty')


def count_letters(phrase):
    N = []
    K = []
    for i in phrase:
        if i.isupper():
            N.append(i)
        elif i.islower():
            K.append(i)
    print(f'Количество заглавных символов: {len(N)}')
    print(f'Количество строчных символов: {len(K)}')


count_letters('Привет, Старина')

# Зачем нужны функции в программировании!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
# уменшают количество строк кода
import turtle


def move(a):
    turtle.forward(a)
    turtle.left(90)


def drewSquare(a):
    for i in range(4):
        move(a)


def drewSquareColor(a, color):
    turtle.color(color)
    turtle.begin_fill()
    drewSquare(a)
    turtle.end_fill()


turtle.speed(3)

drewSquareColor(60, 'red')
turtle.goto(150, 150)
drewSquareColor(120, 'blue')


# Передача аргументов. Сопоставление аргументов по имени и позиции
def f(a, b):
    print(id(a), id(b), 'local')
    a = 100
    b = 200
    print(a, b, 'local')


c = 20
d = 50
f(c, d)  # во время передачи происходит автоматическое присвоение
print(c, d, 'global')
print(id(c), id(d), 'global')


# варианты вызова функции
def e(a, b, c):
    print(a, b, c)


# 1) позиционный
e(1, 5, 7)
# 2) по имени
e(b=10, c=20, a=5)
# комбинированный вариант
e(2, c=10, b=20)  # сначала позиционный аргументы потом именнованные


def t(a, b='None', o='неизвестно'):
    print(a, b, o)


t(1)
t(2, 3)
t(2, 3, 4)  # с перезапишиться


# ОЧЕНЬ ВАЖНО
# не используйте изменеяемые объекты в качетве значенией по умолчанию
def append_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    print(my_list)


a = [1, 2, 4]
append_to_list(10, [2, 3, 4])
append_to_list(10, a)
append_to_list(15, a)
append_to_list(77)


def append_to_dict(key, value, my_dict=None):
    if my_dict is None:
        my_dict = {}

    my_dict[key] = value
    print(my_dict)


append_to_dict(10, 100)
append_to_dict(10, 15)
append_to_dict(20, 200, {'a': 100})

# Вложенные функции в Python
g = 'gray'


def colors(param='r'):
    y = 'yelow'
    g = 'green'

    def print_red():
        r = 'red'
        print(r)
        y = ' was change'

    def print_blue():
        b = 'blue'
        print(b)

    if param == 'r':
        print_red()
    elif param == 'b':
        print_blue()
    else:
        print('i do know this color')


colors('r')


