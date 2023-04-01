# This file will contain the hyphae classes for the game
import pygame

class slimeHyphae(pygame.sprite.Sprite):
    def __init__(self, color, height, width, kind, paintkind):
        super().__init__()

        self.kind = kind
        self.paintkind = paintkind
        self.color = color
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        
        pygame.draw.rect(self.image,
                        color,
                        pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()  
    
    def paint_kind(self):
        if sprite_dict[self.rect.x, self.rect.y].kind == 'food_sprite':
            trait_point_dict[self.paintkind[-1:]] += 1
        sprite_dict[self.rect.x, self.rect.y].setKind(self.paintkind)

    def move(self, dx, dy):
        """
        Move the hyphae by the given amount of pixels in the x and y directions.

        Parameters:
        dx (int): the number of pixels to move the hyphae in the x direction.
        dy (int): the number of pixels to move the hyphae in the y direction.
        """

        self.rect.move_ip(dx, dy)
        self.paint_kind()
        # check that the current self get_loc is within the dimensions of the world 
        # and if it is move the hyphae
        if (self.rect.x + dx >= 0 and self.rect.x + dx <= world_dimensions[0] -12)  and (self.rect.y + dy >= 0 and self.rect.y + dy <= world_dimensions[1] -12):
            self.rect.move_ip(dx, dy)
            self.paint_kind()
            