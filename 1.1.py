import random
a = int(input("Максимальная длинна"))
b = int(input("Максимальное значение"))
def fun(n,m):
    list = []
    for i in range(n):
        list.append(random.randint(0, m));
    return list
print(fun(a, b))



