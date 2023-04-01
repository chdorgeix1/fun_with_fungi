# this file will contain species objects 
# a species object has:
# - a hyphae
# - sprites
# - a trait point counter
# - a trait tree
# - a size counter
# - 

class DurableFungiSpecies(hyphae, sprites, trait_point_counter, size_counter):
    # this class will contain the species object
    def __init__(self, hyphae, sprites, trait_tree, trait_point_counter, size_counter):
        super().__init__()
        self.hyphae = hyphae
        self.sprites = sprites
        self.trait_tree = trait_tree
        self.trait_point_counter = trait_point_counter
        self.size_counter = size_counter        

class PoisonFungiSpecies(hyphae, sprites, trait_point_counter, size_counter):
    # this class will contain the species object
    def __init__(self, hyphae, sprites, trait_tree, trait_point_counter, size_counter):
        super().__init__()
        self.hyphae = hyphae
        self.sprites = sprites
        self.trait_tree = trait_tree
        self.trait_point_counter = trait_point_counter
        self.size_counter = size_counter  
        
class SlimeMoldSpecies(hyphae, sprites, trait_point_counter, size_counter):
    # this class will contain the species object
    def __init__(self, hyphae, sprites, trait_tree, trait_point_counter, size_counter):
        super().__init__()
        self.hyphae = hyphae
        self.sprites = sprites
        self.trait_tree = trait_tree
        self.trait_point_counter = trait_point_counter
        self.size_counter = size_counter  