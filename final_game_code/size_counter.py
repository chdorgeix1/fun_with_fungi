import pygame
from dataclasses import dataclass

@dataclass
class SizeCounter():
    """
    A dataclass representing a trait point counter.
    """
    organism_size: int = 0