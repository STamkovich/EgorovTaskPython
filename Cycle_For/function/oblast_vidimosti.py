#  Область видимости: локальная, глобальная и встроенная
# локальная область выидимости создаётся внутри функции
def s():
    a, b, c = 1, 2, 4
    print(a, b, c)  # переменные видны только внутри функции


def q():
    r, t = 1, 5
    w = 'HELLO'  # локальная переменная
    print(id(w))
    print(r, t, w)  # так же внутри функции нельзя обращаться к переменным другой функции


w = 'hello'  # глобальные переменные - это любые переменные которые вы создаёте вне функции
y = 100


def t():
    a = 11
    b = 22
    c = 33
    print(a, b, c, 'local')


# если убрать локальную переменную то ей присвоится значение глобальной переменной
a = 100
b = 200
c = 300
print(a, b, c, 'global')
s()
q()
t()


# если внутри функции вам необходими изменить значение глобальной переменой
#  вы можете использовать инструкцию global
#  после не неё вы указываете какую хотите использовать глобальную переменную
def f():
    global a
    a = 30


a = [1, 2, 3, 4, 5, 6]
f()
print(a, 'global')


# ВСтроенная область видимости
# в эту область видимисоти входять все встроенные функции объекты и переменные
# что бы увидеть весь список встроенной области видимости нужно нажать ctr + space
def k():
    abs = 10
    print(abs)


def w(x):
    return x ** 2


abs = w
min, max = max, min # так же можно переопределить функции min и max
print(abs(-7), abs(5))


def g():
    # local
    abs = 200
    def q():
        abs = 'hello'
        print((abs, 'q'))
    q()
    print((abs, 'g'))

# global
abs = [1, 2, 3]
g()

# Правила поиска имён в питоне
def i():
    # local
    abs = 200
    def q():
        nonlocal abs
        abs = 'hello'
        print((abs, c, 'q'))
    q()
    print((abs, c, 'i'))

# global
c = 333
abs = [1, 2, 3]
i()

# задачка
# Напишите функцию, которая имя и возраст водителя. 
# Функция должна распечатать на экран заключение, 
# может ли данный водитель управлять транспортом и определять она должна это по возрасту водителя: 
# он должен быть больше или равен MIN_DRIVING_AGE
# Если водитель может управлять, выведите фразу "<name> может водить> " ,
# в противном случае "<name> еще рано садиться за руль" 
# 
# MIN_DRIVING_AGE = 18
# allowed_driving('tim', 17) # выведет "tim еще рано садиться за руль"
# allowed_driving('bob', 18) # выведет "bob может водить"
