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

A.set_color('red')

sprite_list = TestGroup()

sprite_list.add(A)
sprite_list.add(B)
sprite_list.add(C)

for sprite in sprite_list:
    print(sprite.color)
print('')
sprite_list.update()

for sprite in sprite_list:
    print(sprite.color)

print('')

sprite_list.change_group_color('purple')

sprite_list.update()

for sprite in sprite_list:
    print(sprite.color)