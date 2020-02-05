import random

user = str(input("Оставьте тут милый комент:3"))

def fun(a,b,c):
    text ={ a : random.randint(b,c)}
    return text

print (fun(user, 2020, 2100))