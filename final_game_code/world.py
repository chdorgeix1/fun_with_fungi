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
        self.sprite_dict = {}
        pygame.display.set_caption("Fungal Warfare")
        self.clock = pygame.time.Clock()
        #self.pygame.display.flip()
    
    def generate_dimensions(self):
        if self.world_size == 'small':
            self.sprite_size = [15, 15]
            self.dimensions = [self.sprite_size[0]*20 + 5 * 21, self.sprite_size[1]*20 + 5 *21]
        elif self.world_size == 'medium':
            self.sprite_size = [10, 10]
            self.dimensions = [self.sprite_size[0]*20 + 5 * 21, self.sprite_size[1]*20 + 5 *21]
        elif self.world_size == 'large':
            self.sprite_size = [5, 5]
            self.dimensions = [self.sprite_size[0]*20 + 3 * 21, self.sprite_size[1]*20 + 3 *21]
        
    def generate_map(self):
        self.map = pygame.display.set_mode(self.dimensions)
        self.map.fill((200,200,200))


    def draw_sprites(self):
        for i in range(self.sprite_size[0]/3, self.world_size[0], self.sprite_size[0]/3 + self.sprite_size[0]):
            for j in range(self.sprite_size[0]/3, self.world_size[1], self.sprite_size[0]/3 + self.sprite_size[0]):
                if random.random() < 0.99:
                    y = NeutralSprite(i, j, self.sprite_size[0], self.sprite_size[1], color = (0, 0, 0))
                else:
                    y = FoodSprite(10, 10, i, j, self.sprite_size[0], self.sprite_size[1], color = (0, 255, 0))
                self.all_sprites.add(y)
                self.sprite_dict.update({(y.rect[0], y.rect[1]): y})
            
    


def generateWorld(world_dimensions, player1species, player2species):
    #Colors
    BLACK = (0,0,0)
    RED = (255,100,0)
    BLUE = (0, 0, 255)
    ORANGE = (255, 100, 0)
    GREEN =  (0, 200, 200)
    TRUEGREEN = (0, 255, 0)
    DARKGREEN = (0, 200, 100)
    PURPLE = (128, 0, 128)
    trait_point_dict = {RED: 0, BLUE: 0, GREEN: 0, DARKGREEN: 0}
    # World Options
    world_color = (200,200,200)
    sprite_size = [10, 10]
    
    if player1species == 0:
        P1Hyphae = DurableHyphae(GREEN, sprite_size[0], sprite_size[1], 'hyphae', 'armor_sprite_1')
    
    if player1species == 1:
        P1Hyphae = slimeHyphae(RED, sprite_size[0], sprite_size[1], 'hyphae', 'slime_sprite_1')

    if player1species == 2:
        P1Hyphae = poisonHyphae(PURPLE, sprite_size[0], sprite_size[1], 'hyphae', ['poison_sprite_1', 'exp_sprite_1'])

    if player2species == 0:
        P2Hyphae = DurableHyphae(GREEN, sprite_size[0], sprite_size[1], 'hyphae', 'armor_sprite_2')
    

    if player2species == 1:
        P2Hyphae = slimeHyphae(RED, sprite_size[0], sprite_size[1], 'hyphae', 'slime_sprite_2')

    if player2species == 2:
        P2Hyphae = poisonHyphae(PURPLE, sprite_size[0], sprite_size[1], 'hyphae', ['poison_sprite_2', 'exp_sprite_2'])

    
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
