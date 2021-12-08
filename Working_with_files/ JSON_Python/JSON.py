# Работаем с JSON в Python. Парсинг JSON, сохраняем JSON в файл
# JSON - это текстовый формат обменна данными
# преобразуем в пеновский объект при помощи
# функция load когда мы считываем файлик json
# loads когда мы считываем строку в формате json
# метод damp создаёт файлик
# метод damps создаёт строку в виде json
import json
from random import randint
from datetime import datetime
str_json = """
{
    "response": {
        "count": 5961878,
        "items": [{
            "first_name": "Елизавета",
            "id": 620471795,
            "last_name": "Сопова",
            "can_access_closed": true
        }, {
            "first_name": "Роман",
            "id": 614752515,
            "last_name": "Малышев",
            "can_access_closed": true
        }]
    }
}"""
print(type(str_json))

data = json.loads(str_json)
print(type(data))  # проверяем какой тип объекта
# так как items список можно его обойти циклом for
for item in data["response"]["items"]:
    print(item["first_name"], item["last_name"])
    # этим мы распарсили эту джейсонину

# создаём собственную джейсонину
for item in data["response"]["items"]:
    del item['id']  # удаляем один ключ
    item['a'] = None  # добавляем None в джесоне это будет null
    item['likes'] = randint(100, 200)  # добавляем словарь лайков
    item['now'] = datetime.now().strftime('%d/%m/%y')  # нужно преобразовать в одному из пазовых типов который поддерживает джесон
print(data["response"]["items"])
# создаём новую джейсонину из нового словарика
new_json = json.dumps(data, indent=2)  # функция dumps к которой мы передаём объект который хотим превратить в джесон
print(new_json)
# очень часто джесон нужно будет сохранять в виде файла
with open('my.json', 'w') as file:  # создаём файл
    json.dump(data, file, indent=3) # indent для красоты вывода

with open("my_json", 'r') as file:  # загружаем наши данные из файлика в переменную data
    date = json.load(file)
print(data)