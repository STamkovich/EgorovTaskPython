# Возвращаемое значение функции. Оператор return
# встроенные функции
a = abs(-7)
b = max(1, 2, 3, abs(-90), 4, 5, 6, min(80, 100))
print(a)
print(b)


# возвращаемое значение - это то значение которое подставлеться на место вызова функции

# самописные функции
def square(x):
    print(x ** 2)


# def square(x):
#     print(x ** 2)
#     return None
a = square(6)
print(a)


# любая фуекция в питоне возвращает какое либо значение при помощи команды return но если return не указан
# она возвращает None
def square(x):
    return x ** 2


a = square(square(3))  # тут так же идёт вложенный вызов функции
print(a)


def exemple():
    print(1)
    print(2)
    return 'hello'
    print(3)
    print(4)


# return внутри функции работает как brake в цыкле то есть как только попадаешь на return
# автоматически происходит выход из функции
print(exemple())


def even(x):
    if x % 2:
        return True
    else:
        return False


for i in range(1, 11):
    print(i, even(i))


# можно написать короче
def even(x):
    if x % 2:
        return x % 2 == 0


for i in range(1, 11):
    print(i, even(i))


# функция которая находит n число по К
def factotial(x):
    pr = 1
    for i in range(2, x + 1):
        pr = pr * i
    return pr


def sochet(n, k):
    return factotial(n) / (factotial(k) * factotial(n - k))


print(sochet(5, 3))


def sqAndPer(a, b):
    mas = []
    mas.append(a * b)
    mas.append(2 * (a + b))
    return mas


print(sqAndPer(2, 6))
# задачки
# Ваша задача написать функция find_duplicate, которая принимает один аргумент - список чисел.
# Функция должна возвращать список из дублей, каждый дубль нужно брать только один раз в том порядке,
# в котором они встречаются в исходном списке. Под дублем будем подразумевать число,
# которое присутствовало в списке несколько раз.
# Ваша задача написать только определение функции
def find_duplicate(x):
    y = []
    for i in x:
        if x.count(i) > 1:
            if i not in y:
                y.append(i)
    return y


print(find_duplicate([1, 2, 3, 4, 4, 3, 5]))

# Напишите функцию factorial, которая принимает на вход одно неотрицательное число,
# и возвращает значение факториала данного числа.
def factorial(x):
    pr = 1
    for i in range(2, x + 1):
        pr = pr * i
    return pr

print(factorial(abs(5)))

# Напишите функцию first_unique_char,
# которая принимает строку символов и возвращает позицию первого уникального символа в строке.
# В случае, если уникальных символов в переданной строке нет, верните -1.
# Регистр символов не учитывайте.
def first_unique_char(x) -> object:
    for i in x:
        if x.count(i) == 1:
            return x.index(i)
    return -1
print(first_unique_char('!#$@#@!'))

# Ваша задача написать функцию format_namelist, которая принимает список словарей,
# у каждого словаря в списке есть только ключ name
# Функция format_namelist должна вернуть отформатированную строку,
# в которой все имена из списка разделяются запятой кроме последних двух имен, они должны быть разделены союзом "и".
# Если в списке нет ни одного имени, функция должна вернуть пустую строку. Ниже представлены примеры:
def format_namelist(x):
    y = []
    for i in range(len(x)):
        y.append(x[i]['name'])
    for i in y:
        if len(y) == 1:
            return print(y[0])
        elif len(y) > 1:
            return print((', '.join(y[:-1])) + ' и ' + y[-1])
    return "''"
