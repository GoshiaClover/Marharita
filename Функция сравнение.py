import random

a = int(input("Максимальная длинна списка: "))
b = int(input("Максимальное значение списка: "))
c = int(input("Максимальная длинна списка: "))
d = int(input("Максимальное значение списка: "))

def fun (q,w,e,r):
    list1 = []
    for n in range(q):
        list1.append(random.randint(0, w))

    list2 = []
    for m in range(e):
        list2.append(random.randint(0, r))

    list3 = []
    for s in list1:
        if s in list2:
            list3.append(s)

    if len(list3) == 0:
        print("Совпадений нет")
    else:
        return list(set(list3))
print(fun(a,b,c,d))

