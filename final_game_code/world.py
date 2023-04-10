# this file will generate the world for the game
import pygame
import random
from pygame.sprite import Group
from pygame.time import Clock
from sprite import FoodSprite, NeutralSprite, ImpassSprite, DurableSprite
from species import DurableFungiSpecies, PoisonFungiSpecies, SlimeMoldSpecies
from player import DurablePlayer, PoisonPlayer, SlimePlayer

# this class will generate the world for the game

class World():
    def __init__(self, world_size, player1species, player2species):
        self.world_size = world_size
        self.dimensions = []
        self.sprite_size = []
        self.sprite_dict = {}
        self.player1species = player1species
        self.player2species = player2species
        self.all_sprites = Group()
        pygame.display.set_caption("Fungal Warfare")
        self.clock = Clock()
    
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
        self.map.fill((50,50,50))

    def update_sprite_dict(self, sprite):
        self.sprite_dict.update({(sprite.rect[0], sprite.rect[1]): sprite})

    def draw_sprites(self):
        for i in range(2, self.dimensions[0], 2 + self.sprite_size[0]):
            for j in range(2, self.dimensions[1], 2 + self.sprite_size[1]):
                if random.random() < 0.95:
                    y = NeutralSprite(i, j, self.sprite_size[0], self.sprite_size[1])
                else:
                    y = FoodSprite(i, j, self.sprite_size[0], self.sprite_size[1])
                self.all_sprites.add(y)
                self.update_sprite_dict(y)
            
    def draw_impass(self):
        x_list = list(range(2, self.dimensions[0] + 2 + self.sprite_size[0], 2 + self.sprite_size[0]))
        y_list = list(range(self.dimensions[0], 2 -(2 + self.sprite_size[0]), -(2 + self.sprite_size[0])))

        for i in range(len(x_list)):
            x_list[i] -= int(self.dimensions[0]/60)*(2 + self.sprite_size[0])
        
        for i in zip(x_list, y_list):
            for j in range((-2 - self.sprite_size[0]), 2*(2 + self.sprite_size[0]), 2 + self.sprite_size[0]):
                for impsprite in self.all_sprites.sprites():
                    if impsprite.rect.x == i[0] and impsprite.rect.y == i[1] + j:
                        impsprite.kill()
                        self.all_sprites.add(ImpassSprite(i[0], i[1] + j, self.sprite_size[0], self.sprite_size[1]))

    def generate_players(self):
        if self.player1species == 0:
            Player1 = DurablePlayer()
        elif self.player1species == 1:
            Player1 = PoisonPlayer()
        else:
            Player1 = SlimePlayer()

        if self.player2species == 0:
            Player2 = DurablePlayer()
        elif self.player2species == 1:
            Player2 = PoisonPlayer()
        else:
            Player2 = SlimePlayer()
        
        return Player1, Player2
    
    def draw_players(self, Player1, Player2):
        if random.random() > 0.5:
            p1start = [2, 2]
            p2start = [self.dimensions[0] - 2 - self.sprite_size[0], self.dimensions[1] - 2 - self.sprite_size[1]]
        else:
            p1start = [self.dimensions[0] - 2 - self.sprite_size[0], self.dimensions[1] - 2 - self.sprite_size[1]]
            p2start = [2, 2]
        
        P1StartSprite = Player1.base_sprite(p1start[0], p1start[1], self.sprite_size[0], self.sprite_size[1], Player1.base_traits.attack_score, Player1.base_traits.defense_score, Player1.base_traits.growth_rate, color = (0,180,0))
        P2StartSprite = Player2.base_sprite(p2start[0], p2start[1], self.sprite_size[0], self.sprite_size[1], Player2.base_traits.attack_score, Player2.base_traits.defense_score, Player2.base_traits.growth_rate, color = (180, 0, 0))
        
        print(P1StartSprite)
        print(P2StartSprite)


        Player1.group.add(P1StartSprite)
        Player2.group.add(P2StartSprite)
        
        self.all_sprites.add(P1StartSprite)
        self.all_sprites.add(P2StartSprite)
        self.update_sprite_dict(P1StartSprite)
        self.update_sprite_dict(P2StartSprite)


