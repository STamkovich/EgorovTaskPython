# Декоратор это функция внутрь которой входит еще какая либо функция выполнение которой дополняет функция декоратор,
# в декораторе также присутствует замыкание.
# Проще говоря декоратор это функция дополняющая функцию которая входит в декоратор.
# Давайте напишем декоратор в котором будем здороваться с именем переданным как аргумент.
# Def decorator(func): #Создаем функцию (имя не имеет значения) которую я так и назвал – decorator.
# Внутрь нее передаем аргумент func, Этот аргумент будет являться функцией.
# Def inner(): – #Создаем вложенную функцию
# Print(‘Привет’)
# Print(‘Дорогой’)
# Func() – далее вызываем функцию которую мы передали в функции декоратор.
# Func(*args, **kwargs) – передаем непроизвольное количество аргументов,
# Так как мы в консоли будем писать имя человека с которым здороваемся
# Для того чтобы аргументы передались, мы их должны получить.
# Получать будем из функции inner() внутрь которой также будет передавать непроизвольное количество аргументов:
# Def inner(*args, **kwargs): выглядит это так
# Return inner возвращаем функцию return() чтобы получилось замыкание
# Def names(name): создаем функцию names() которая принимает аргумент name. В name будем передавать имя.
# Функция names передается в функцию decorator(func) – аргументом func
# Print(name)  выводим имя.
# Вот код который получился:
def decorator(func):
    def inner(*args, **kwargs):
        print('Привет')
        print('Дорогой')
        func(*args, **kwargs)

    return inner


def names(name):
    print(name)


# Теперь есть два варианта вывода  имени, Первый:
names = decorator(names)
# В оператор names кладем функцию decorator которая принимает аргумент names который является функцией names
names(input())  # вызываем функцию names  в которую передаем имя которое запишем через коносль input’ом
# На выходе получается так:
names = decorator(names)
names(input())


# Второй вариант которым следует пользоваться:
@decorator  # навешиваем функцию decorator через @
def names(name):
    print(name)  # Функция на которую навешиваем декоратор


names(input())  # передаем имя через консоль.


# На выходе:
@decorator
def names(name):
    print(name)


names('boq')


# В обоих случаях код выведет это (в аргумент name передадим имя Иван):
# Привет
# Дорогой
# Иван
# подробнее про декораторы по этой ссылке https://stepik.org/lesson/63305/step/1

def decator(func):
    def inner():
        print('start decorator')
        func()
        print('finish decorator')

    return inner()


def say():
    print('hello world')


def buy():
    print('buy world')


say = decator(say)
say()

buy = decator(buy)
buy()


# пример с несколькими декораторами
def header(func):
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('/h1')

    return inner


def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    return inner


@table
@header  # say = header(say)
def say(name, surname, age):
    print('hello', name, surname, age)


say('Vanya', 'ivanov', 30)


# У декорированных функций есть одна проблема.
# А именно декорированная функция теряет свое имя а также документацию после декорирования.
# Будем использовать данный декоратор:
def decorator(func):
    def tags(vivod, tag):
        print(f'<{tag}>')
        func(vivod)
        print(f'</{tag}>')
    return tags


# Создадим декорируемую функцию которая просто возвращает квадрат числа.
def sqr(x):
    return x ** 2


# открываем консоль
# Сейчас к нашей функции можно обратиться и узнать ее имя таким способом: sqr.__name__ =  sqr
# .__name__ =  Это волшебный оператор который показывает имя функции. Как видим сейчас к нашей функции можно обратиться.
# Теперь задекорируем фунцию sqr:
# Sqr = decorator(sqr) – попробуем обратиться к ней:
# Sqr.__name__ =  tags. Как видим теперь при обращении к нашей функции у нее имя не sqr а tags.
# Это происходит потому что мы задекорировали эту фукцию в декораторе который возвращает функцию tags.
# Так же у функций могут быть документации:
def sqr(x):
    """
    Функция sqr возвращает

          Квадрат числа x
    :param x:
    :return:
    """
    print(x ** 2)


# К этой документации можно обратиться при помощи функции help() – help(sqr):
# Help on function sqr in module __main__:
sqr(x)  # Функция возводит в     квадрат число x
# Как видите документацию мы можем увидеть.
# Теперь задекорируем функцию – sqr = decorator(sqr)
# Help(sqr) - Help on function tags in module __main__:
# tags(vivod, tag)
# Снова та же ошибка. Декорированная функция не может быть прочтена.
# Эта проблема решаемая и тут к нам на помощь приходит виновник торжества: decorator @wraps
# Импортируем его из модуля func toold
from functools import wraps


def decorator(func):
    @wraps(func)
    def tags(vivod, tag):
        print(f'<{tag}>')
        func(vivod)
        print(f'</{tag}>')

    return tags


# Вешаем декоратор @wraps на функцию inner и передаем ему аргументом декорируемую фунцию @wraps(func)
# Теперь декорируем нашу фунцию и обращаемся к ней.
sqr = decorator(sqr)
# help(sqr):
# Help on function sqr in module __main__:
sqr(x)
#     Функция возводит в
#
#     квадрат число x
#
# sqr.__name__  - sqr
