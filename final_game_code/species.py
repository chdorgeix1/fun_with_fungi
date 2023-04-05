# this file will contain species objects 

import pygame
from dataclasses import dataclass
from hyphae import DurableHyphae 
from sprite_group import DurableSpriteGroup
from sprite_traits import DurableSpriteTraits
from trait_tree import DurableTraitTree

from hyphae import PoisonHyphae
from sprite_group import PoisonSpriteGroup
from sprite_traits import PoisonSpriteTraits
from trait_tree import PoisonTraitTree

from hyphae import SlimeHyphae
from sprite_group import SlimeSpriteGroup
from sprite_traits import SlimeSpriteTraits
from trait_tree import SlimeTraitTree

class DurableFungiSpecies(DurableHyphae, DurableSpriteGroup, DurableSpriteTraits, DurableTraitTree):
    # this class will contain the species object
    def __init__(self):
        super().__init__()

    def move_hyphae(self):
        self.add(pygame.get_sprite_at(self.move()))

class PoisonFungiSpecies(PoisonHyphae, PoisonSpriteGroup, PoisonSpriteTraits, PoisonTraitTree):
    # this class will contain the species object
    def __init__(self):
        super().__init__()

    def move_hyphae(self):
        self.add(pygame.get_sprite_at(self.move()))

class SlimeMoldSpecies(SlimeHyphae, SlimeSpriteGroup, SlimeSpriteTraits, SlimeTraitTree):
    # this class will contain the species object
    def __init__(self):
        super().__init__()

    def move_hyphae(self):
        self.add(pygame.get_sprite_at(self.move()))
        self.add(pygame.get_sprite_at(self.move()))
