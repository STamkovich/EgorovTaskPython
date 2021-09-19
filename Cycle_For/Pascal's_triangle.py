# Треугольни Паскаля
#      1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
# значения которые мы получаем в каждом реду называются бинаминальными кофициетами и
# и они используются в формуле бинома Ньютона
# (a + b)**n то есть (a + b)**2 = (1)a**2 + 2ab + (1)b**2
#                    (a + b)**3 = a**3 + 3a**2b + 3ab**2 + b**3
# (a + b)**4 = 1a**4b**0 + 4a**3b**1 + 6a**2b**2 + 4a**1b**3 + 1a**0b**4
n = int(input())
triangle = []
for i in range(n + 1):
    triangle.append([1] + [0] * n)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        triangle[i][j] = triangle[i - 1][j] + triangle[i - 1][j - 1]

for i in range(0, n + 1):
    for j in range(0, n + 1):
        print(triangle[i][j], end=' ')
    print()
