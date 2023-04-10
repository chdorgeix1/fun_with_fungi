# this file will be the final game file that combines all of the other files

import pygame
import sprite
import hyphae
import species
import random
from pygame.sprite import Group
from world import World

new_world = World('large', 0, 2)

new_world.generate_dimensions()

new_world.generate_map()

new_world.draw_sprites()

new_world.draw_impass()

Player1, Player2 = new_world.generate_players()

new_world.draw_players(Player1, Player2)

pygame.init()
exit = False
count = 0
global combined_sprites
combined_sprites = Group()
combined_sprites.add(Player1.group.sprites())
combined_sprites.add(Player2.group.sprites())

def grow_cell_sprites():
    global combined_sprites
    cell_list = list(range(0,len(combined_sprites)))

    for i in range(len(combined_sprites)):
        x = random.choice(cell_list)
        cell_list.remove(x)
        example_sprite = combined_sprites.sprites()[x]
        if example_sprite.growing == True:
            if example_sprite in Player1.group:
                example_sprite.grow(sprite_dict = new_world.sprite_dict, all_sprites = new_world.all_sprites, self_group = Player1.group, combined_sprites_group = combined_sprites)
            elif example_sprite in Player2.group:
                example_sprite.grow(sprite_dict = new_world.sprite_dict, all_sprites = new_world.all_sprites, self_group = Player2.group, combined_sprites_group = combined_sprites)

while not exit:
    count += 1
    if count%100 == 0:
        for sprites in new_world.all_sprites.sprites():
            sprites.growing = True
    
    grow_cell_sprites()

    #Player1.group.group_grow(sprite_dict = new_world.sprite_dict, all_sprites = new_world.all_sprites)

    #Player2.group.group_grow(sprite_dict = new_world.sprite_dict, all_sprites = new_world.all_sprites)

    new_world.all_sprites.draw(new_world.map)
        #new_world.map.fill((0,200,200))

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit = True
    new_world.clock.tick(50)
