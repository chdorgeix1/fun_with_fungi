# This file will contain the hyphae classes for the game
import pygame
from abc import ABC, abstractmethod
from pygame.sprite import Sprite

class BaseHyphae(ABC, Sprite):
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

class DurableHyphae(BaseHyphae):
    """
    A sprite representing a durable hyphae.
    """

    def __init__(self):
        """
        Initialize a new instance of the DurableHyphae class.

        Parameters:
        color (tuple): the RGB color of the hyphae.
        height (int): the height of the hyphae in pixels.
        width (int): the width of the hyphae in pixels.
        kind (str): the kind of the hyphae.
        paintkind (str): the paint kind of the hyphae.
        """
        super().__init__(color = (0,255,0), height = 20, width = 20)
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

    def move(self, dx, dy):
        """
        Move the hyphae by the given amount of pixels in the x and y directions.

        Parameters:
        dx (int): the number of pixels to move the hyphae in the x direction.
        dy (int): the number of pixels to move the hyphae in the y direction.
        """
        self.rect.move_ip(dx, dy)
        return(self.rect.x, self.rect.y)

class PoisonHyphae(BaseHyphae):
    """
    A sprite representing a durable hyphae.
    """

    def __init__(self):
        """
        Initialize a new instance of the DurableHyphae class.

        Parameters:
        color (tuple): the RGB color of the hyphae.
        height (int): the height of the hyphae in pixels.
        width (int): the width of the hyphae in pixels.
        kind (str): the kind of the hyphae.
        paintkind (str): the paint kind of the hyphae.
        """
        super().__init__(color = (0,0,255), height = 20, width = 20)

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

    def move(self, dx, dy):
        """
        Move the hyphae by the given amount of pixels in the x and y directions.

        Parameters:
        dx (int): the number of pixels to move the hyphae in the x direction.
        dy (int): the number of pixels to move the hyphae in the y direction.
        """
        self.rect.move_ip(dx, dy)
        return(self.rect.x, self.rect.y)
    
class SlimeHyphae(BaseHyphae):
    """
    A sprite representing a durable hyphae.
    """
    def __init__(self):
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
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

    def move(self, dx, dy):
        """
        Move the hyphae by the given amount of pixels in the x and y directions.

        Parameters:
        dx (int): the number of pixels to move the hyphae in the x direction.
        dy (int): the number of pixels to move the hyphae in the y direction.
        """
        self.rect.move_ip(dx, dy)
        return(self.rect.x, self.rect.y)