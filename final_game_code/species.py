# this file will contain species objects 

import pygame
from hyphae import DurableHyphae, PoisonHyphae, SlimeHyphae
from sprite_group import DurableSpriteGroup, PoisonSpriteGroup, SlimeSpriteGroup
from sprite_traits import DurableSpriteTraits, PoisonSpriteTraits, SlimeSpriteTraits
from trait_tree import DurableTraitTree, PoisonTraitTree, SlimeTraitTree

class DurableFungiSpecies(DurableHyphae, DurableSpriteGroup):
    # this class will contain the species object
    def __init__(self, sprite_traits = DurableSpriteTraits, trait_tree = DurableTraitTree):
        super().__init__()
        self.traits = sprite_traits
        self.trait_tree = trait_tree

    def move_hyphae(self):
        self.add(pygame.get_sprite_at(self.move()))

class PoisonFungiSpecies(PoisonHyphae, PoisonSpriteGroup):
    # this class will contain the species object
    def __init__(self, sprite_traits = PoisonSpriteTraits, trait_tree = PoisonTraitTree):
        super().__init__()
        self.traits = sprite_traits
        self.trait_tree = trait_tree

    def move_hyphae(self):
        self.add(pygame.get_sprite_at(self.move()))

class SlimeMoldSpecies(SlimeHyphae, SlimeSpriteGroup):
    # this class will contain the species object
    def __init__(self, sprite_traits = SlimeSpriteTraits, trait_tree = SlimeTraitTree):
        super().__init__()
        self.traits = sprite_traits
        self.trait_tree = trait_tree

    def move_hyphae(self):
        self.add(pygame.get_sprite_at(self.move()))
        self.add(pygame.get_sprite_at(self.move()))
