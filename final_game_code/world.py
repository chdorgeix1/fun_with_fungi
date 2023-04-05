# this file will generate the world for the game
import pygame
import random
from sprite import FoodSprite, NeutralSprite, ImpassSprite, DurableSprite

# this class will generate the world for the game

class World():
    def __init__(self, world_size, player1species, player2species):
        self.world_size = world_size
        self.dimensions = []
        self.sprite_size = []
        self.player1species = player1species
        self.player2species = player2species
        self.all_sprites = pygame.sprite.Group()
        pygame.display.set_caption("Fungal Warfare")
        self.clock = pygame.time.Clock()
        #self.pygame.display.flip()
    
    def generate_dimensions(self):
        if self.world_size == 'small':
            self.sprite_size = [15, 15]
            self.dimensions = [int(self.sprite_size[0]*64 + 2 * 65), int(self.sprite_size[1]*40 + 2 *41)]
        elif self.world_size == 'medium':
            self.sprite_size = [9, 9]
            self.dimensions = [self.sprite_size[0]*96 + 2 * 97, self.sprite_size[1]*60 + 2 *61]
        elif self.world_size == 'large':
            self.sprite_size = [6, 6]
            self.dimensions = [self.sprite_size[0]*150 + 2 * 151, self.sprite_size[1]*90 + 2 *91]
        
    def generate_map(self):
        self.map = pygame.display.set_mode(self.dimensions)
        self.map.fill((200,200,200))

    #int(self.sprite_size[0]/3)
    def draw_sprites(self):
        for i in range(2, self.dimensions[0], 2 + self.sprite_size[0]):
            for j in range(2, self.dimensions[1], 2 + self.sprite_size[1]):
                if random.random() < 0.59:
                    y = NeutralSprite(i, j, self.sprite_size[0], self.sprite_size[1])
                else:
                    y = FoodSprite(i, j, self.sprite_size[0], self.sprite_size[1])
                self.all_sprites.add(y)
            
    


def generateWorld(world_dimensions, player1species, player2species):


    
    food_rate = 0.01

    sample_surface = pygame.display.set_mode((world_dimensions[0], world_dimensions[1]))
    sample_surface.fill((200,200,200))
    all_sprites_list = pygame.sprite.Group()

    for i in range(2, world_dimensions[0]-6, 12):
        for j in range(2, world_dimensions[1]-6, 12):
            if random.random() > 0.99:
                y = Sprite(sprite_size[0], sprite_size[1], i, j, 'food_sprite')
            else:
                y = Sprite(sprite_size[0], sprite_size[1], i, j, 'base_sprite')
            all_sprites_list.add(y)
            sprite_dict.update({(y.rect[0], y.rect[1]): y})

    P1Hyphae.rect.x = 470
    P1Hyphae.rect.y = 470

    P2Hyphae.rect.x = 26
    P2Hyphae.rect.y = 26

    sprite1 = sprite_dict[470,470]      

    sprite2 = sprite_dict[26,26]      

    if player1species == 0:
        sprite1.setKind('durable_sprite_1')

    if player1species == 1:
        sprite1.setKind('slime_sprite_1')

    if player1species == 2:
        sprite1.setKind('poison_sprite_1')

    if player2species == 0:
        sprite2.setKind('durable_sprite_2')

    if player2species == 1:
        sprite2.setKind('slime_sprite_2')

    if player2species == 2:
        sprite2.setKind('poison_sprite_2')

    all_sprites_list.add(sprite1)
    all_sprites_list.add(P1Hyphae)
    all_sprites_list.add(sprite2)
    all_sprites_list.add(P2Hyphae)
    pygame.init()

    return all_sprites_list, sample_surface, P1Hyphae, P2Hyphae
