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

# задчки
# Анализ продаж
# К вам в руки попал файлик формата json , в котором содержится информация одного автосалона о продажах менеджеров.
# В файле указано для каждого менеджера список проданных им автомобилей,
# а также проставлена цена продажи каждого автомобиля.
# Ваша задача скачать файлик и самостоятельно найти самого успешного менеджера по итоговой сумме продаж.
# В качестве ответа нужно через пробел указать сперва его имя, затем фамилию и после общую сумму его продаж.
import json

with open('/home/sergey/PycharmProjects/EgorovTaskPython/Working_with_files/ JSON_Python/manager_sales.json', 'r') as file:
    data = json.load(file)
# print(data)
# print(type(data))  # проверяем какой тип объекта

max_summa = 0
name_manager = ''
last_name_manager = ''
for item in data:
    summa = sum([i['price'] for i in item['cars']])
    if summa > max_summa:
        max_summa = summa
        name_manager = item['manager']['first_name']
        last_name_manager = item['manager']['last_name']
print(name_manager, last_name_manager, max_summa)

# В json-файле содержится информация о нескольких групп людей, при этом у каждой группы есть свой идентификатор.
# Ваша задача скачать файлик и самостоятельно найти идентификатор группы,
# в которой находится самое большое количество женщин, рожденных после 1977 года.
# В качестве ответа необходимо указать через пробел идентификатор найденной группы и сколько в ней было женщин,
# рожденных после 1977 года.
with open('/home/sergey/PycharmProjects/EgorovTaskPython/Working_with_files/ JSON_Python/group_people.json', 'r') as file:
    data = json.load(file)
# print(data)


max_count = 0
id_group = 0
for id in data:
    count = 0
    for person in id['people']:
        if person['gender'] == 'Female' and person['year'] > 1977:
            count += 1
    if count > max_count:
        max_count = count
        id_group = id['id_group']
print(id_group, max_count)
# В этой задаче вам необходимо раскодировать текст, находящийся в данном текстовом файле.
# Ключ для декодирования располагается в json-файле. В качестве ответа нужно просто отправить получившийся текст.
# И обратите внимание, что раскодировать нужно только лишь буквы,
# все остальные символы(цифры, знаки пунктуации и т.д.) необходимо выводить как есть.
file = open('/home/sergey/PycharmProjects/EgorovTaskPython/Working_with_files/ JSON_Python/Alphabet.json', 'r')
data = json.load(file)
file.close()
# print(data)
file_text = open('/home/sergey/PycharmProjects/EgorovTaskPython/Working_with_files/ JSON_Python/Abracadabra.txt',
                 'r', encoding='utf-8')
text = file_text.read()
file_text.close()
# print(text)
decoded = []
for letter in text:
    decoded.append(data.get(letter, letter))
stroka = ''.join(decoded)
print(stroka)
# Переменная people содержит строку в формате JSON, в которой вы можете получить личные данные 100 человек.
# Каждого человека представляет предмет (словарь) с ключами:
# имя
# страна
# возраст
# Распечатайте информацию о каждом человеке в соответствии с примером ниже.
# Melissa Crawford, Lebanon, 17
# Paul Herrera, Kiribati, 17
# Justin Galvan, Namibia, 19
# Mary Estes, Montenegro, 19
# Larry Bray, Brunei Darussalam, 21
# <Имя>, <Страна>, <Возраст>
# Распечатку необходимо отсортировать по возрасту, а при равенстве возраста необходимо расположить в алфавитном порядке
import json
people = '[' \
         '{"name": "Haley Whitney", "country": "British Indian Ocean Territory (Chagos Archipelago)", "age": 54}, ' \
         '{"name": "Matthew King", "country": "Colombia", "age": 34}, ' \
         '{"name": "Sean Sullivan", "country": "Mayotte", "age": 40}, ' \
         '{"name": "Christian Crawford", "country": "Russian Federation", "age": 29}, ' \
         '{"name": "Sarah Contreras", "country": "Honduras", "age": 82}, ' \
         '{"name": "Danielle Williams", "country": "Togo", "age": 91}, ' \
         '{"name": "Jonathan Wilson", "country": "Tunisia", "age": 49}, ' \
         '{"name": "Patricia Wilkerson", "country": "Georgia", "age": 22}, ' \
         '{"name": "Zachary Scott", "country": "Brunei Darussalam", "age": 55}, ' \
         '{"name": "Elizabeth Sanchez", "country": "Nauru", "age": 23}, ' \
         '{"name": "Christina Fernandez", "country": "Burundi", "age": 71}, ' \
         '{"name": "Allen Norton", "country": "Montserrat", "age": 79}, ' \
         '{"name": "Scott Arroyo", "country": "Montenegro", "age": 72}, ' \
         '{"name": "Brooke Boyd", "country": "Latvia", "age": 74}, ' \
         '{"name": "Jerry Morrow", "country": "San Marino", "age": 23}, ' \
         '{"name": "Danielle Bradshaw", "country": "Vietnam", "age": 64}, ' \
         '{"name": "Jerry Thompson", "country": "Belgium", "age": 30}, ' \
         '{"name": "Mark Jordan", "country": "Comoros", "age": 89}, ' \
         '{"name": "Joseph Berger", "country": "Cook Islands", "age": 94}, ' \
         '{"name": "Gina Brooks", "country": "Samoa", "age": 51}, ' \
         '{"name": "Walter Duran", "country": "Chad", "age": 67}, ' \
         '{"name": "John Martinez", "country": "Wallis and Futuna", "age": 65}, ' \
         '{"name": "Johnny Glover", "country": "Eritrea", "age": 72}, ' \
         '{"name": "Lindsay Moore", "country": "Liberia", "age": 53}, ' \
         '{"name": "Kimberly Burton", "country": "Nicaragua", "age": 92}, ' \
         '{"name": "Jacqueline Ballard", "country": "Nigeria", "age": 78}, ' \
         '{"name": "Charles Thompson", "country": "Saudi Arabia", "age": 50}, ' \
         '{"name": "Suzanne Roberts", "country": "Serbia", "age": 43}, ' \
         '{"name": "David Decker", "country": "South Africa", "age": 71}, ' \
         '{"name": "Christopher Perez", "country": "Cayman Islands", "age": 49}, ' \
         '{"name": "Debra Hall", "country": "Greece", "age": 13}, ' \
         '{"name": "John King", "country": "Bahamas", "age": 40}, ' \
         '{"name": "Justin Galvan", "country": "Namibia", "age": 19}, ' \
         '{"name": "Jacqueline Berger", "country": "Yemen", "age": 59}, ' \
         '{"name": "Shawn Robinson", "country": "Saint Pierre and Miquelon", "age": 32}, ' \
         '{"name": "Kristen Garcia", "country": "Portugal", "age": 48}, ' \
         '{"name": "Christopher Barry", "country": "French Polynesia", "age": 23}, ' \
         '{"name": "Alejandra Cook", "country": "Egypt", "age": 16}, ' \
         '{"name": "Jill Harrell", "country": "Comoros", "age": 49}, ' \
         '{"name": "Sara Zimmerman", "country": "Brazil", "age": 26}, ' \
         '{"name": "Mrs. Charlene Flores", "country": "New Caledonia", "age": 75}, ' \
         '{"name": "Melissa Crawford", "country": "Lebanon", "age": 17}, ' \
         '{"name": "Larry Wong", "country": "New Caledonia", "age": 6}, ' \
         '{"name": "Brenda Acosta", "country": "Grenada", "age": 48}, ' \
         '{"name": "Latoya Terry", "country": "Saint Martin", "age": 41}, ' \
         '{"name": "Seth Luna", "country": "Sao Tome and Principe", "age": 59}, ' \
         '{"name": "Micheal Adams", "country": "Barbados", "age": 53}, ' \
         '{"name": "Susan Carroll", "country": "Somalia", "age": 64}, ' \
         '{"name": "Douglas Morris", "country": "Thailand", "age": 24}, ' \
         '{"name": "Dennis Wagner", "country": "Zimbabwe", "age": 66}, ' \
         '{"name": "Kristin Johnson", "country": "Niue", "age": 71}, ' \
         '{"name": "Steven Krause", "country": "Turkmenistan", "age": 84}, ' \
         '{"name": "Jared Smith", "country": "Colombia", "age": 46}, ' \
         '{"name": "Lauren Anderson", "country": "Christmas Island", "age": 46}, ' \
         '{"name": "Joshua Spencer", "country": "Russian Federation", "age": 38}, ' \
         '{"name": "Maria Edwards", "country": "Hungary", "age": 78}, ' \
         '{"name": "Anne Lee", "country": "United States of America", "age": 10}, ' \
         '{"name": "James Mckenzie", "country": "Uganda", "age": 43}, ' \
         '{"name": "Joshua Gallegos", "country": "United States Minor Outlying Islands", "age": 27}, ' \
         '{"name": "Paul Herrera", "country": "Kiribati", "age": 17}, ' \
         '{"name": "Veronica White", "country": "Gabon", "age": 88}, ' \
         '{"name": "Michael Hall", "country": "China", "age": 43}, ' \
         '{"name": "Sabrina Thompson", "country": "Chad", "age": 27}, ' \
         '{"name": "Jennifer Archer", "country": "Korea", "age": 45}, ' \
         '{"name": "Christina Simmons", "country": "Israel", "age": 80}, ' \
         '{"name": "Travis White", "country": "Central African Republic", "age": 31}, ' \
         '{"name": "Dennis Hernandez", "country": "Slovenia", "age": 66}, ' \
         '{"name": "Matthew Richards", "country": "Svalbard & Jan Mayen Islands", "age": 34}, ' \
         '{"name": "Stephen Curry", "country": "Finland", "age": 92}, ' \
         '{"name": "Margaret Williamson", "country": "Hong Kong", "age": 86}, ' \
         '{"name": "Mary Estes", "country": "Montenegro", "age": 19}, ' \
         '{"name": "Alex Scott", "country": "Christmas Island", "age": 67}, ' \
         '{"name": "John Andrews", "country": "Bahamas", "age": 68}, ' \
         '{"name": "Jonathan Willis", "country": "Saint Martin", "age": 23}, ' \
         '{"name": "Olivia Campos", "country": "Armenia", "age": 72}, ' \
         '{"name": "Diana Davis", "country": "Azerbaijan", "age": 54}, ' \
         '{"name": "Jack Cummings", "country": "Martinique", "age": 94}, ' \
         '{"name": "Kaitlyn Mcdonald", "country": "Austria", "age": 12}, ' \
         '{"name": "Maria Blake", "country": "Pitcairn Islands", "age": 91}, ' \
         '{"name": "Kelly Thomas", "country": "Ethiopia", "age": 74}, ' \
         '{"name": "John Terrell Jr.", "country": "India", "age": 50}, ' \
         '{"name": "Lindsay Wood", "country": "United Arab Emirates", "age": 72}, ' \
         '{"name": "Matthew Gilbert", "country": "Madagascar", "age": 86}, ' \
         '{"name": "Tanner Johnson", "country": "Congo", "age": 11}, ' \
         '{"name": "Michael Garcia", "country": "Liberia", "age": 45}, ' \
         '{"name": "Nicole Johnson", "country": "Barbados", "age": 54}, ' \
         '{"name": "William Lee", "country": "Lithuania", "age": 59}, ' \
         '{"name": "Jeffrey Coffey", "country": "Faroe Islands", "age": 88}, ' \
         '{"name": "Sandra Freeman", "country": "Philippines", "age": 35}, ' \
         '{"name": "Latoya Maxwell", "country": "Sweden", "age": 12}, ' \
         '{"name": "Darius Blevins", "country": "Thailand", "age": 29}, ' \
         '{"name": "Teresa Newman", "country": "Jersey", "age": 6}, ' \
         '{"name": "Larry Bray", "country": "Brunei Darussalam", "age": 21}, ' \
         '{"name": "Adam Roberson", "country": "Jordan", "age": 71}, ' \
         '{"name": "Michael Gomez", "country": "Tajikistan", "age": 37}, ' \
         '{"name": "Abigail Mccarthy", "country": "Kiribati", "age": 85}, ' \
         '{"name": "Tom Morris", "country": "Cayman Islands", "age": 27}, ' \
         '{"name": "Kevin Wagner", "country": "Suriname", "age": 55}, ' \
         '{"name": "Peggy Bryant", "country": "Korea", "age": 36}, ' \
         '{"name": "Erik Mclaughlin", "country": "Austria", "age": 24}' \
         ']'
# print(type(people))
data = json.loads(people)
# print(type(data))
lst = sorted(data, key=lambda x: (x['age'], x['name']))
for i in lst:
    print(f'{i["name"]}, {i["country"]}, {i["age"]}')