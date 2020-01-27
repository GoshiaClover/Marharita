import random

list = [0, 1,2,3,4,5,6,7,8,9]
random.shuffle(list)
print(list)
del list[-1]
print(list)


