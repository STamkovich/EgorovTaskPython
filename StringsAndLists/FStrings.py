                                            # F-строки
gender = {
    'm': "Дорогой",
    'n': "Дорогая"
}
a = [
    ['Андрей', 'Владимировичь', 767.33, 'm'],
    ['Виктория', 'Сергеевна', 345.44, 'n'],
    ['Ксения', 'Андреевна', 355, 'n']
]

for name, mid_name, balance, g in a:
    text = f'''{gender[g]} {name} {mid_name}, баланс вашего лицевого счёта состовляет {balance} руб.'''
    print(text)

# в f строках  можно производить манипуляции сложения, умножени и т.д так же использовать методы
# примеры
# put your python code here
a = input()
text = f"Мое имя {a}!"
print(text)

name = input().upper()
age = input()
text = f'Hello {name}. You are {age} years old.'
print(text)

rate = float(input())
dollar = int(input())
text1 = f"Current dollar rate is {rate}. You want buy {dollar} dollars\nYou"
text2 = f"must pay {rate * dollar}"
print(text1, text2)

name = input()
year = int(input())

text = f"{name}, вам исполнится 77 лет в {year + 77} "
print(text)

a = int(input())
b = int(input())
print(f'''{a} / {b} = {a / b}\n{a} // {b} = {a // b}\n{a} % {b} = {a % b}''')


