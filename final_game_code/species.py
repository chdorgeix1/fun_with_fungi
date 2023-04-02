# this file will contain species objects 
# a species object has:
# - a hyphae
# - sprites
# - a trait point counter
# - a trait tree
# - a size counter
import pygame
from dataclasses import dataclass

class DurableFungiSpecies():
    # this class will contain the species object
    def __init__(self):
        super().__init__()
        # self.hyphae = hyphae DONE
        # self.sprites = sprites
        # self.trait_tree = trait_tree DONE
        # self.trait_point_counter = trait_point_counter DONE
        # self.size_counter = size_counter 

    class DurableHyphae(pygame.sprite.Sprite):
        """
        A sprite representing a durable hyphae.
        """

        def __init__(self, kind = 'durable_fungi', paintkind = 'chitin_fungi', color = (255,0,0), height = 20, width = 20):
            """
            Initialize a new instance of the DurableHyphae class.

            Parameters:
            color (tuple): the RGB color of the hyphae.
            height (int): the height of the hyphae in pixels.
            width (int): the width of the hyphae in pixels.
            kind (str): the kind of the hyphae.
            paintkind (str): the paint kind of the hyphae.
            """
            super().__init__()
            self.color = color
            self.height = height
            self.width = width
            self.kind = kind
            self.paintkind = paintkind
            self.image = pygame.Surface([self.width, self.height])
            self.image.fill(self.color)
            self.rect = self.image.get_rect()

        def paint_kind(self, world_sprite_dict, player_trait_point_dict):
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

    @dataclass
    class DurableTraitTree():
        short_tough_wall: int = 0
        short_impenetrable_wall: int = 0
        long_impenetrable_wall: int = 0 #defensive wall

        armored_cells_grow: int = 0
        stronger_armored_cells: int = 0 # improved armored cells

        spread_spores: int = 0
        longer_spore_range: int = 0
        larger_spores: int = 0 #spore spreading ability

        ultimate: int = 0 
    
    @dataclass
    class TraitPointCounter():
        trait_point_counter: int = 0

# class PoisonFungiSpecies(hyphae, sprites, trait_point_counter, size_counter):
#     # this class will contain the species object
#     def __init__(self, hyphae, sprites, trait_tree, trait_point_counter, size_counter):
#         super().__init__()
#         self.hyphae = hyphae
#         self.sprites = sprites
#         self.trait_tree = trait_tree
#         self.trait_point_counter = trait_point_counter
#         self.size_counter = size_counter  
        
# class SlimeMoldSpecies(hyphae, sprites, trait_point_counter, size_counter):
#     # this class will contain the species object
#     def __init__(self, hyphae, sprites, trait_tree, trait_point_counter, size_counter):
#         super().__init__()
#         self.hyphae = hyphae
#         self.sprites = sprites
#         self.trait_tree = trait_tree
#         self.trait_point_counter = trait_point_counter
#         self.size_counter = size_counter  