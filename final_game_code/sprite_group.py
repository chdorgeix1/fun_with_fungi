# this sprite will contain the sprite groups for each species
# This file will contain the sprite class for the game
import pygame
import random
from abc import ABC, abstractmethod
from pygame.sprite import Group

class BaseGroup(ABC, Group):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def group_grow(self):
        None 

class DurableSpriteGroup(BaseGroup):
    def __init__(self):
        super().__init__()

    def group_grow(self):
        for sprite in self.sprites():
            sprite.grow()

class PoisonSpriteGroup(BaseGroup):
    def __init__(self):
        super().__init__()

    def group_grow(self):
        for sprite in self.sprites():
            sprite.grow()

class SlimeSpriteGroup(BaseGroup):
    def __init__(self):
        super().__init__()

    def group_grow(self):
        for sprite in self.sprites():
            sprite.grow()