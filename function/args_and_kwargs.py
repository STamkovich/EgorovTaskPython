# *args и **kwargs Python. Передача аргументов в функцию
# оператор *
a, *b, c = [True, 7, 'hello', 9, '54', 3]
print(a, b, c)

a, *b, c = 'hello world'
print(a, b, c)

s = [4, 10]
print(list(range(1, 5)))
print(list(range(*s)))


# здесь оператор * использовали внутри вызова функции при передачи
# и он распаковывал значение при передачи по локальным переменным
def f(a, b, c, d):
    print(a, b, c, d)


f(1, 2, 3, 4)
a = ('hello', True, 78, [3, 4, 5])

f(*a)


# здесь мы будем оператор * использовать при определении нашеё функции
def f(*args):
    s = 0
    for i in args:
        s += i
    return s


f(1, 2, 3, 4, 5, 5)
print(f(1, 2))


# здесб мы будем передавать в функцию именнованные аргументы и внеограниченном количестве

def t(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


t(a=1, b=5, name=6)


def i(*args, **kwargs):
    print(args, kwargs)


def outPrint(*args, sep="#", end="@"):
    print(args, sep, end)


i(1, 2, 3, 4, 5, b=5, name=6)
outPrint(1, 2, 3, 4, 5, 5, sep='90')

a = [3, 4, 5, 6, 7]
print(*a)


# задачки
# Напишите функцию count_args, которая принимает произвольное количество аргументов.
# Данная функция должна возвращать количество переданных ей на вход аргументов
def count_args(*args):
    count = 0
    for i in args:
        count += 1
    return count

# Давайте теперь создадим функцию print_goods, которая печатает список покупок.
# На вход она будет принимать произвольное количество значений, а товаром мы будем считать любые непустые строки.
# То есть числа, списки, словари и другие нестроковые объекты вам нужно будет проигнорировать.
# Функция print_goods должна печатать список товаров в виде: <Порядковый номер товара>. <Название товара>.
# В случае, если в переданных значениях не встретится ни одного товара, необходимо распечатать текст "Нет товаров"


def print_goods(*args):
    count = 0
    product = 0
    for i in args:
        count += 1
        if type(i) == str and i != '':
            print(f"{count}. {i}")
            product += 1
    if product == 0:
        print("Нет товаров")

print_goods()

# Напишите функцию info_kwargs, которая принимает произвольное количество именованных аргументов.
# Функция info_kwargs должна распечатать именованные аргументы в каждой новой строке в виде пары <Ключ> = <Значения>,
# причем ключи должны следовать в алфавитном порядке. Пример работы смотрите ниже


def info_kwargs(**kwargs):
    list_keys = list(kwargs.keys())
    list_keys.sort()

    for i in list_keys:
        print(i, '=', kwargs[i])


info_kwargs(first_name="John", last_name="Doe", age=33)