# this file will contain species objects 

import pygame
from hyphae import DurableHyphae, PoisonHyphae, SlimeHyphae
from sprite_group import DurableSpriteGroup, PoisonSpriteGroup, SlimeSpriteGroup
from sprite_traits import DurableSpriteTraits, PoisonSpriteTraits, SlimeSpriteTraits
from trait_tree import DurableTraitTree, PoisonTraitTree, SlimeTraitTree

class DurableFungiSpecies(DurableHyphae, DurableSpriteGroup):
    # this class will contain the species object
    def __init__(self, DurableSpriteTraits, DurableTraitTree):
        super().__init__()
        self.traits = DurableSpriteTraits
        self.trait_tree = DurableTraitTree

    def move_hyphae(self):
        self.add(pygame.get_sprite_at(self.move()))

class PoisonFungiSpecies(PoisonHyphae, PoisonSpriteGroup):
    # this class will contain the species object
    def __init__(self, PoisonSpriteTraits, PoisonTraitTree):
        super().__init__()
        self.traits = PoisonSpriteTraits
        self.trait_tree = PoisonTraitTree

    def move_hyphae(self):
        self.add(pygame.get_sprite_at(self.move()))

class SlimeMoldSpecies(SlimeHyphae, SlimeSpriteGroup):
    # this class will contain the species object
    def __init__(self, SlimeSpriteTraits, SlimeTraitTree):
        super().__init__()
        self.traits = SlimeSpriteTraits
        self.trait_tree = SlimeTraitTree

    def move_hyphae(self):
        self.add(pygame.get_sprite_at(self.move()))
        self.add(pygame.get_sprite_at(self.move()))
