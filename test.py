numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = list(map(lambda x: x ** 2, numbers))
m = list(map(lambda x: x ** 3, numbers))
print(n, m, sep='\n')
