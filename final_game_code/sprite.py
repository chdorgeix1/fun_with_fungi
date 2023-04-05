# This file will contain the sprite class for the game
import pygame
import random
from abc import ABC, abstractmethod
from pygame.sprite import Sprite

class BaseSprite(ABC, Sprite):
    def __init__(self, x_loc, y_loc, attack_score, defense_score, height, width, color):
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
    def grow(self):
        None 

class NeutralSprite(BaseSprite):
    def __init__(self, x_loc, y_loc, height, width, attack_score = 0, defense_score = 0): 
        super().__init__(x_loc, y_loc, height, width, attack_score, defense_score, 10, 10, (0,0,0))

    def getAttributes(self, kind):   
        None
    
    def grow(self):
        None 

class FoodSprite(BaseSprite):
    def __init__(self, x_loc, y_loc, attack_score = 0, defense_score = 0):
        super().__init__(x_loc, y_loc, attack_score, defense_score, 10, 10, (0,255,0))

    def getAttributes(self, kind):   
        None
    
    def grow(self):
        None 

class ImpassSprite(BaseSprite):
    def __init__(self, x_loc, y_loc, attack_score = 0, defense_score = 1000): 
        super().__init__(x_loc, y_loc, attack_score, defense_score, 10, 10, (100,100,100))

    def getAttributes(self, kind):   
        None
    
    def grow(self):
        None 

class DurableSprite(BaseSprite):
    def __init__(self, x_loc, y_loc, attack_score = 15, defense_score = 15): 
        super().__init__(x_loc, y_loc, attack_score, defense_score, 10, 10, (0,100,0))

    def getAttributes(self, kind):   
        None
    
    def grow(self):
        None 

class ChitinSprite(BaseSprite):
    def __init__(self, x_loc, y_loc, attack_score = 25, defense_score = 50): 
        super().__init__(x_loc, y_loc, attack_score, defense_score, 10, 10, (0,200,0))

    def getAttributes(self, kind):   
        None
    
    def grow(self):
        None 