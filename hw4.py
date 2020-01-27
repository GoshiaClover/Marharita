import random

a = random.randint(0, 10)
b = random.randint(0, 10)
c = random.randint(0, 10)

if a > b:
    print("Котики милашки:3")
if a < b:
    print("Зима без снега")
if a == b:
    print(str(c) + str("А теперь эта!"))
    print(c + (a+b))
    if (a+b)>c:
        print("Солнышко яркое")
    if (a+b)< c:
        print("Завтра рано вставать")
    if (a+b)== c:
        print("Страдания")
