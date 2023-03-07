import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
import time
arr_size = 20
x = np.zeros((arr_size,arr_size))

y = 1

def print_array(x):
    for line in x:
        print(line)

print_array(x)

target_num = [5, 16]

for i in range(10):
    for p in range(10):
        if i < 3:
            a = (np.random.randint(0,6))
            b = (np.random.randint(0,6))
        else:
            a = (np.random.randint(0,6)) - 3
            b = (np.random.randint(0,6)) - 3
        #if ((i + a) <= arr_size and (i + a) >= 0) and ((i + b) <= arr_size and (i + b) >= 0): 
            #for j in zip(range(a), range(b)):
        x[np.abs(target_num[0] - i) + i/2][np.abs(target_num[0] - i) + i/2] = y

                #x[i + j[0]][i] = y
                #x[i][i + j[0]] = y

        print_array(x)
        print('')
        time.sleep(1)