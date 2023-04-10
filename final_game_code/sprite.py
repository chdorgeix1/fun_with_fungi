# This file will contain the sprite class for the game
import pygame
import random
from abc import ABC, abstractmethod
from pygame.sprite import Sprite

class BaseSprite(ABC, Sprite):
    def __init__(self, x_loc, y_loc, height, width, attack_score, defense_score, color):
        super().__init__()
        self.height = height
        self.width = width
        self.attack_score = attack_score
        self.defense_score = defense_score
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.color = color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()        
        self.rect.x = x_loc
        self.rect.y = y_loc

    @abstractmethod
    def getAttributes(self, kind):   
        None
    
    @abstractmethod
    def grow(self, sprite_dict):
        None 

class NeutralSprite(BaseSprite):
    def __init__(self, x_loc, y_loc, height, width, attack_score = 0, defense_score = 0): 
        super().__init__(x_loc, y_loc, height, width, attack_score, defense_score, (0,0,0))

    def getAttributes(self, kind):   
        None
    
    def grow(self, sprite_dict):
        None 

class FoodSprite(BaseSprite):
    def __init__(self, x_loc, y_loc, height, width, attack_score = 0, defense_score = 0):
        super().__init__(x_loc, y_loc, height, width, attack_score, defense_score, (100,200,0))

    def getAttributes(self, kind):   
        None
    
    def grow(self, sprite_dict):
        None 

class ImpassSprite(BaseSprite):
    def __init__(self, x_loc, y_loc, height, width, attack_score = 0, defense_score = 1000): 
        super().__init__(x_loc, y_loc, height, width, attack_score, defense_score, (92, 64, 51))

    def getAttributes(self, kind):   
        None
    
    def grow(self, sprite_dict):
        None 

class DurableSprite(BaseSprite):
    def __init__(self, x_loc, y_loc, height, width, attack_score, defense_score, growth_rate, color): 
        super().__init__(x_loc, y_loc, height, width, attack_score, defense_score, color)
        self.growth_rate = growth_rate
        self.growing = True
    def getAttributes(self, kind):   
        None
    
    def grow(self, sprite_dict, all_sprites, self_group, combined_sprites_group):
        if self.growing:
            not_grow_count = 0
            for i in range(-self.width - 2, 2 * (self.width + 2), self.width + 2):
                for j in range(-self.height - 2, 2 * (self.height + 2), self.height + 2):
                    if (self.x_loc + i, self.y_loc + j) in sprite_dict:
                        new_sprite = sprite_dict[(self.x_loc + i, self.y_loc + j)]
                        if new_sprite not in self_group:
                            if random.random() < self.growth_rate:
                                new_sprite.kill()
                                grow_sprite = DurableSprite(self.x_loc + i, self.y_loc + j, self.height, self.width, self.attack_score, self.defense_score, self.growth_rate, self.color)
                                sprite_dict[(self.x_loc + i,self.y_loc + j)] = grow_sprite
                                self_group.add(grow_sprite)
                                all_sprites.add(grow_sprite)
                                combined_sprites_group.add(grow_sprite)
                        else:
                            not_grow_count += 1
                    if not_grow_count > 3:
                        self.growing = False

        


class ChitinSprite(BaseSprite):
    def __init__(self, x_loc, y_loc, height, width, attack_score, defense_score, growth_rate): 
        super().__init__(x_loc, y_loc, height, width, attack_score, defense_score, (0,200,0))
        self.growth_rate = growth_rate
        self.growing = True

    def getAttributes(self, kind):   
        None
    
    def grow(self):
        None 

class PoisonSprite(BaseSprite):
    def __init__(self, x_loc, y_loc, height, width, attack_score, defense_score, growth_rate, color): 
        super().__init__(x_loc, y_loc, height, width, attack_score, defense_score, color)
        self.growth_rate = growth_rate
        self.growing = True
        
    def getAttributes(self, kind):   
        None
    
    def grow(self, sprite_dict, all_sprites, self_group, combined_sprites_group):
        if self.growing:
            not_grow_count = 0
            for i in range(-self.width - 2, 2 * (self.width + 2), self.width + 2):
                for j in range(-self.height - 2, 2 * (self.height + 2), self.height + 2):
                    if (self.x_loc + i, self.y_loc + j) in sprite_dict:
                        new_sprite = sprite_dict[(self.x_loc + i, self.y_loc + j)]
                        if new_sprite not in self_group:
                            if random.random() < self.growth_rate:
                                new_sprite.kill()
                                grow_sprite = PoisonSprite(self.x_loc + i, self.y_loc + j, self.height, self.width, self.attack_score, self.defense_score, self.growth_rate, self.color)
                                sprite_dict[(self.x_loc + i,self.y_loc + j)] = grow_sprite
                                self_group.add(grow_sprite)
                                all_sprites.add(grow_sprite)
                                combined_sprites_group.add(grow_sprite)
                        else:
                            not_grow_count += 1
                    if not_grow_count > 3:
                        self.growing = False

class ExplosiveSprite(BaseSprite):
    def __init__(self, x_loc, y_loc, height, width, attack_score, defense_score, growth_rate, color): 
        super().__init__(x_loc, y_loc, height, width, attack_score, defense_score, color)
        self.growth_rate = growth_rate

    def getAttributes(self, kind):   
        None
    
    def grow(self):
        None 

class SlimeSprite(BaseSprite):
    def __init__(self, x_loc, y_loc, height, width, attack_score, defense_score, growth_rate, color): 
        super().__init__(x_loc, y_loc, height, width, attack_score, defense_score, color)
        self.growth_rate = growth_rate
        self.growing = True
    def getAttributes(self, kind):   
        None
    
    def grow(self, sprite_dict, all_sprites, self_group, combined_sprites_group):
        if self.growing:
            not_grow_count = 0
            for i in range(-self.width - 2, 2 * (self.width + 2), self.width + 2):
                for j in range(-self.height - 2, 2 * (self.height + 2), self.height + 2):
                    if (self.x_loc + i, self.y_loc + j) in sprite_dict:
                        new_sprite = sprite_dict[(self.x_loc + i, self.y_loc + j)]
                        if new_sprite not in self_group:
                            if random.random() < self.growth_rate:
                                new_sprite.kill()
                                grow_sprite = SlimeSprite(self.x_loc + i, self.y_loc + j, self.height, self.width, self.attack_score, self.defense_score, self.growth_rate, self.color)
                                sprite_dict[(self.x_loc + i,self.y_loc + j)] = grow_sprite
                                self_group.add(grow_sprite)
                                all_sprites.add(grow_sprite)
                                combined_sprites_group.add(grow_sprite)
                        else:
                            not_grow_count += 1
                    if not_grow_count > 3:
                        self.growing = False