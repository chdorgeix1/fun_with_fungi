# this file will contain species objects 

import pygame
from hyphae import DurableHyphae, PoisonHyphae, SlimeHyphae
from sprite_group import DurableSpriteGroup, PoisonSpriteGroup, SlimeSpriteGroup
from sprite_traits import DurableSpriteTraits, PoisonSpriteTraits, SlimeSpriteTraits, ExplosiveSpriteTraits, ChitinSpriteTraits
from trait_tree import DurableTraitTree, PoisonTraitTree, SlimeTraitTree
from sprite import DurableSprite, PoisonSprite, SlimeSprite, ExplosiveSprite, ChitinSprite


class DurableFungiSpecies(DurableHyphae, DurableSpriteGroup):
    # this class will contain the species object
    def __init__(self):
        super().__init__()
        self.base_sprite = DurableSprite
        self.extra_sprite = ChitinSprite
        self.base_traits = DurableSpriteTraits
        self.extra_traits = ChitinSpriteTraits
        self.trait_tree = DurableTraitTree

    def move_hyphae(self):
        self.add(pygame.get_sprite_at(self.move()))

class PoisonFungiSpecies(PoisonHyphae, PoisonSpriteGroup):
    # this class will contain the species object
    def __init__(self):
        super().__init__()
        self.base_sprite = PoisonSprite
        self.extra_sprite = ExplosiveSprite
        self.base_traits = PoisonSpriteTraits
        self.extra_traits = ExplosiveSpriteTraits
        self.trait_tree = PoisonTraitTree

    def move_hyphae(self):
        self.add(pygame.get_sprite_at(self.move()))

class SlimeMoldSpecies(SlimeHyphae, SlimeSpriteGroup):
    # this class will contain the species object
    def __init__(self):
        super().__init__()
        self.base_sprite = SlimeSprite
        self.base_traits = SlimeSpriteTraits
        self.trait_tree = SlimeTraitTree

    def move_hyphae(self):
        self.add(pygame.get_sprite_at(self.move()))
        self.add(pygame.get_sprite_at(self.move()))
