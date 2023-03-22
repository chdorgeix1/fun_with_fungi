import random
global x
x = 5
#print(x)
def changeX():
    global x
    x = x + 2
    return x
changeX()
#print(x)

example_dict = {'multiple_hyphae': 1, 'piercing_hyphae': 1}
y = 5
if example_dict['multiple_hyphae'] == 1:
    y += 1
print('y:', y)    