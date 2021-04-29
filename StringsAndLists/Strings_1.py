# Cтроки и операции над ними
n = '''hello
world
hey
'''
print(n)
# сложение строк
s = 'hello'
g = 'world'
print(s + g)
# умножение строк
e = s * 3
print(e)
# нахождение длинны строки
t = len('hello')
print(t)
q = input()
print("Вы ввели", len(q), 'символов')
# проверка есть ли символ в строке
i = "!2#$%%^567"
print('6' in i)
# сравнение строк
w = 'aaa' == 'aaa'
print(w)
w1 = "aaa" > 'er'
print(w1)
# получение числового значения
r = ord('a')  # ascii code table узнать код значения
print(r)
# задачки
a = 'Я стану крутым программистом!'
print(a, a, a, sep='\n')

print(input() + "\n" + input())

a = input()
b = input()
c = input()
print(c, b, a, sep="\n")

print((input() + ' ') * 4)

print("Лев Николаевич Толстой написал \"Война и мир\"")
