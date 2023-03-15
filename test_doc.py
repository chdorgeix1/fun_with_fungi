import random
close_dict = {1:(-1,1), 2:(0,1), 3:(1,1), 4:(1,0), 5:(1,-1), 6:(0,-1), 7:(-1,-1), 8:(-1,0)}

direction = random.choice(list(close_dict.items()))
#print(len(close_dict))
#print(direction)
del close_dict[direction[0]]
#print(len(close_dict))

for x in range(1,3):
    print('x:', x)
    for i in range(-x, x+1):
        for j in range(-x, x+1):
            print('Combination:', i, " ", j)