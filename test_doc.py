import random

rand_list = list(range(0,10))

print(rand_list)

for i in range(len(rand_list)):
    x = random.choice(rand_list)
    rand_list.remove(x)

print(rand_list)