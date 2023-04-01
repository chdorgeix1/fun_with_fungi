# This file will contain the hyphae classes for the game
import pygame
from abc import ABC, abstractmethod

class BaseHyphae(ABC, pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.color = color
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def paint_kind(self):
        pass

class DurableHyphae(BaseHyphae):
    """
    A sprite representing a durable hyphae.
    """

    def __init__(self, kind = 'durable_fungi', paintkind = 'chitin_fungi'):
        """
        Initialize a new instance of the DurableHyphae class.

        Parameters:
        color (tuple): the RGB color of the hyphae.
        height (int): the height of the hyphae in pixels.
        width (int): the width of the hyphae in pixels.
        kind (str): the kind of the hyphae.
        paintkind (str): the paint kind of the hyphae.
        """
        super().__init__(color = (255,0,0), height = 20, width = 20)
        self.kind = kind
        self.paintkind = paintkind
        
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def paint_kind(self):
        """
        Paint the hyphae with the current paint kind.
        """
        sprite = sprite_dict[self.rect.x, self.rect.y]
        if sprite.kind == 'food_sprite':
            trait_point_dict[self.paintkind[-1:]] += 1
        sprite.setKind(self.paintkind)

    def move(self, dx, dy):
        """
        Move the hyphae by the given amount of pixels in the x and y directions.

        Parameters:
        dx (int): the number of pixels to move the hyphae in the x direction.
        dy (int): the number of pixels to move the hyphae in the y direction.
        """
        dest_x = self.rect.x + dx
        dest_y = self.rect.y + dy
        self.rect.move_ip(dx, dy)
        self.paint_kind()