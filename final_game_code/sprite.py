# This file will contain the sprite class for the game
import pygame
import random
from abc import ABC, abstractmethod

class BaseSprite(ABC, pygame.sprite.Sprite):
    def __init__(self, x_loc, y_loc, height, width, color):
        super().__init__()
        self.height = height
        self.width = width
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.color = color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()        
        self.rect.x = x_loc
        self.rect.y = y_loc

    # @abstractmethod
    # def setKind(self, new_kind):
    #     pass
    
    # @abstractmethod
    # def getAttributes(self, kind):   
    #     pass
    
    # @abstractmethod
    # def grow(self):
    #     pass 

# q: why am i getting an error at x_loc

# a: 

class FoodSprite(BaseSprite):
    def __init__(self, x_loc, y_loc, kind = 'food_sprite'):
        super().__init__(x_loc, y_loc, 20, 20, (0,255,0))
        self.kind = kind



