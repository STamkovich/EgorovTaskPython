# 10.6 Сортировка коллекций в Python. Метод sort и функция sorted
# sort-метод списков vs sorted-функция

a = [4, -10, 43, -300, 54, 89, -34]
b = 'hello world'
c = ('hi', 'zero', 'abracadabra', 'pikachu')
# метод sort применяется только к спискам
# метод sort изначально меняет коллекцию
a.sort()
print(a)  # [-300, -34, -10, 4, 43, 54, 89]
sorted(a)
sorted(b)  # не изменяет коллекцию
print(b)  # hello world
sorted(c)
# что бы полностью отсортировать  список нужно выполнить присвоение
c = sorted(c)
print(c)  # ['abracadabra', 'hi', 'pikachu', 'zero']
# похожи sort и sorted тем что они принимают два необязательных именнованых аргумента
#  первый называется key(определяет по какому ключу будет выполняться сортировка) и он должен принимать функцию
#  другой reverse() и этот аргумент является типом bool True/False
# b = sorted(b, key=function, reverse=True/False)
# a = sort(key=function, reverse=True/False)
# параметр reverse
b = sorted(b, reverse=True/False)
# по умолчанию принимает значение False(тем самым все элементы сортируются во возрастанию)
# если задать True  то элементы отсортируются по убыванию
# для строк это будет в алфавитном порядке
# функция sorted всегда возвращает список


