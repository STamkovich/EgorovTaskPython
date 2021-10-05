# замыкания

def main_func(name):
    def inner_func():
        print('hello my friend', name)

    return inner_func


# замыканием называется такая ситуация когда вложенная функция пользуется переменными которые не обявлены в её теле
# задачка
# Ваша задача создать функцию multiply, которая принимает один аргумент.
# Функция должна запомнить это значение,
# и вернуть результат умножения этого числа с переданным вновь значением (см. примеры)
# f_2 = multiply(2)
# print("Умножение 2 на 5 =", f_2(5)) #10
# print("Умножение 2 на 15 =", f_2(15)) #30
# f_3 = multiply(3)
# print("Умножение 3 на 5 =", f_3(5)) #15
# print("Умножение 3 на 15 =", f_3(15)) #45
def multiply(value):
    def f_2(a):
        return value * a

    return f_2


f_2 = multiply(2)
f_2(5)
f_2(15)


# примеры замыкания
def averige_nambers():
    nums = []

    def inner(num):
        nums.append(num)
        return sum(nums) / len(nums)


r1 = averige_nambers()
r1(5)
r1(10)

def average_numbers():
    numbers = []

    def inner(number):
        numbers.append(number)
        return sum(numbers) / len(numbers)
        print(numbers)
    return inner()


from time import perf_counter


def time():
    start = perf_counter()

    def inner():
        return perf_counter() - start

    return inner()


def add(a, b):
    return a + b


def counter(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'функция {func.__name__} вызывалась {count} раз')
        return func(*args, **kwargs)

    return inner()
