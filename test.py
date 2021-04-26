# Электронные часы - 2
# Электронные часы показывают время в формате h:mm:ss, то есть сначала записывается количество часов в диапазоне
# от 0 до 23, потом обязательно двузначное количество минут, затем обязательно двузначное количество секунд.
# Количество минут и секунд при необходимости дополняются до двузначного числа нулями.
# Программа получает на вход число n - количество секунд, которое прошло с начала суток.
# Выведите показания часов, соблюдая формат.
n = int(input())
h = (n // 3600) % 24
m = (n // 60) % 60
s = n % 60
print(str(h), str(m).rjust(2, '0'), str(s).rjust(2, '0'), sep=':')

