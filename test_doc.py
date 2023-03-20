import random
global x
x = 5
print(x)
def changeX():
    global x
    x = x + 2
    return x
changeX()
print(x)