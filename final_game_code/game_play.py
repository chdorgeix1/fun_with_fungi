# this file will be the final game file that combines all of the other files

import pygame
import sprite
import game_dicts

p1Sprite = sprite.FoodSprite(5, 5)
#p2Hyphae = hyphae_classes.DurableHyphae(color = (0,255,0), height =20, width = 20)

#q: why am i getting the following erro __init__() got an unexpected keyword argument 'x_loc'

# a: because you are not passing in the x_loc argument in the FoodSprite class

print(p1Sprite.color, p1Sprite.height, p1Sprite.width)
