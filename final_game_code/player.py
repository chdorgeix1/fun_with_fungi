# this file will contain the player class and the necessary functions for the player to interact with the game

import pygame
from species import DurableFungiSpecies, PoisonFungiSpecies, SlimeMoldSpecies
class Player():
    def __init__(self, species):
        self.species = species
        self.size = 1
        self.trait_points = 0
    
    def get_size(self):
        self.size = len(self.species.sprites())
        return self.size
    
    def update_trait_points(self, x):
        self.trait_points = self.trait_points + x
        return self.trait_points

    def get_trait_points(self):
        return self.trait_points
    
    def update_species_tree(self):
        None
        # input the species tree and the trait points
        # update the species tree
        # return the species tree
        # this function will be called when the player presses the button to update the species tree
        # reduce trait points by the cost of the trait

    def get_species_tree(self):
        return self.tree
        # this function will be called when the player presses the button to view the species tree