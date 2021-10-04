# Анонимная функция Lambda
# простая функция
def f(x):
    return x ** 2


print(f(4))
# синтаксис --> lambda арг1, арг2,.... : выражение
r = lambda x: x ** 2
print(r(7))

# lambda используется в тех случаях когда вам необходимо написать функцию в которой выполняется одно только действие или
# функцию в одну строчку
per = lambda a, b, c: a + b + c
print(per(1, 2, 3))
h = lambda: 'hello'
print(h())


# lambda может заменить толко те функции которые что то возвращают(то есть содержиться слова return)
# при помощи Lambda нельзя реализовать функции в которых содержится циклы
def f(x):
    if x > 0:
        return 'positive'
    else:
        return 'nagative'


t = lambda x: 'positive' if x > 0 else 'nagative'
print(t(5))
# использование lambda
# def w(x):
# return x % 10
a = [65, 86, 34, 6, 87, 5456, 786, 55666]
a.sort(key=lambda x: x % 10)
print(a)


def linaer(k, b):
    return lambda x: x * k + b

grafi = linaer(2, 5)
print(grafi(3))
# задачки
# Напишите lambda функцию, которая принимает одно число и увеличивает его на 10.
# Для проверки решения присвойте вашу  lambda функцию переменной adding_10
adding_10 = lambda x: x + 10

print(adding_10(5))

# Напишите lambda функцию, которая принимает строку и отвечает на вопрос начинается ли переданная строка с буквы W
# Для проверки решения присвойте вашу  lambda функцию переменной starts_with
starts_with = lambda x: x[0] == 'W'
print(starts_with('Whtrh'))

# В python есть стандартный модуль datetime.
# Внутри него имеется функция datetime.datetime.now() при помощи которой,
# можно найти текущую дату в формате (год, месяц, день, час, минуты, секунды, млсекунды)
# Ваша задача написать три lambda функция, которые принимают текущую дату и возвращают год, месяц и день соответственно.
# Эти три lambda функции нужно будет сохранить в переменные get_year, get_month и get_day соответственно.
# Вызывать ничего не нужно, просто создайте функции
import datetime

now = datetime.datetime.now()
get_year = lambda x: now.year
get_month = lambda x: now.month
get_day = lambda x: now.day

print(get_year(now), get_month(now), get_day(now))