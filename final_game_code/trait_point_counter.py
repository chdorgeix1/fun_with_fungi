import pygame
from dataclasses import dataclass

@dataclass
class TraitPointCounter():
    """
    A dataclass representing a trait point counter.
    """
    trait_points: int = 0
