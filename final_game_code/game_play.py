# this file will be the final game file that combines all of the other files

import pygame
import sprite
import hyphae
import species
from world import World

new_world = World('small', 0, 1)

new_world.generate_dimensions()

new_world.generate_map()

new_world.draw_sprites()

new_world.draw_impass()

Player1, Player2 = new_world.generate_players()

new_world.draw_players(Player1, Player2)

pygame.init()
exit = False
count = 0

print(new_world.sprite_dict[(2,2)])

while not exit:
    
    Player1.group.group_grow(sprite_dict = new_world.sprite_dict, all_sprites = new_world.all_sprites)

    new_world.all_sprites.draw(new_world.map)
        #new_world.map.fill((0,200,200))

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit = True
    new_world.clock.tick(10)
