# this file will contain data classes for traits of each species

from dataclasses import dataclass

@dataclass
class DurableSpriteTraits():
    attack_score: int = 25
    defense_score: int = 25
    growth_rate: float = 0.05

@dataclass
class ChitinSpriteTraits():
    attack_score: int = 30
    defense_score: int = 50
    growth_rate: float = 0

@dataclass
class PoisonSpriteTraits():
    attack_score: int = 15
    defense_score: int = 15
    growth_rate: float = 0.75

@dataclass
class ExplosiveSpriteTraits():
    attack_score: int = 0
    defense_score: int = 10
    growth_rate: float = 0

@dataclass
class SlimeSpriteTraits():
    attack_score: int = 10
    defense_score: int = 10
    growth_rate: float = 0.9


