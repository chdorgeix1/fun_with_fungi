import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group

class TestSprite(Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.color = 'blue'
    def set_color(self, color):
        self.color = color
    def update(self):
        self.color = 'green'
        
class TestGroup(Group):
    def __init__(self) -> None:
        super().__init__()
        self.color = 'orange'
    def change_group_color(self, color):
        self.color = color

    def update(self):
        for sprite in self:
            sprite.color = self.color

A = TestSprite()
B = TestSprite()
C = TestSprite()

from trait_tree import DurableTraitTree

