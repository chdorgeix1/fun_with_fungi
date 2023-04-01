# this file will be the final game file that combines all of the other files

import pygame
import hyphae_classes
import game_dicts

p1Hyphae = hyphae_classes.DurableHyphae(color = (255,0,0), height =20, width = 20)
p2Hyphae = hyphae_classes.DurableHyphae(color = (0,255,0), height =20, width = 20)

p1Hyphae.move(10,10)

print(p1Hyphae.rect.x, p1Hyphae.rect.y)
print(p2Hyphae.rect.x, p2Hyphae.rect.y)