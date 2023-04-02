# this file will be the final game file that combines all of the other files

import pygame
import sprite
import hyphae
import species
#import game_dicts

# p1Sprite = sprite.FoodSprite(5, 5)
# #p2Hyphae = hyphae_classes.DurableHyphae(color = (0,255,0), height =20, width = 20)

# #q: why am i getting the following erro __init__() got an unexpected keyword argument 'x_loc'

# # a: because you are not passing in the x_loc argument in the FoodSprite class

# print(p1Sprite.__class__ == sprite.FoodSprite)

# print(p1Sprite.color, p1Sprite.height, p1Sprite.width)


P1Species = species.DurableFungiSpecies()
P1Hyphae = P1Species.DurableHyphae()
P1Tree = P1Species.DurableTraitTree()


P2Species = species.DurableFungiSpecies()
P2Hyphae = P2Species.DurableHyphae()
P2Tree = P2Species.DurableTraitTree()

P1Tree.short_tough_wall = 1

print(P1Tree.short_tough_wall)

print(P2Tree.short_tough_wall)

print(P1Hyphae.color, P1Hyphae.height, P1Hyphae.width)