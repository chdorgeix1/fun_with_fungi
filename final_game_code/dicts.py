# this file will contain the kind of sprites and the traits dictionaries for the game


# a: this class is used to create the traits tree for the player

class TraitTree:
    def __init__(self, player_species):
        super().__init__()

        self.tree_kind = player_species
        
        if self.tree_kind == 'slime_mold':
            self.tree = {'splitting_cells': 0, 'plasmodium': 0, 'bouncing_plasmodium': 0,  #plasmodium abilities
                           'random_hyphae': 0, 'seeking_hyphae': 0,'food_hyphae': 0, '2_ai_hyphae': 0, #hyphae abilities
                           'faster_growth':0, 'stronger_attack': 0, 'exponential_growth': 0, #growth increase and EG ability
                           'pierching_hyphae': 0} #ultimate
        
        elif self.tree_kind == 'durable_fungi':
            self.tree = {'short_tough_wall': 0, 'short_impenetrable_wall': 0, 'long_impenetrable_wall': 0, #defensive wall
                            'armored_cells_grow': 0, 'stronger_armored_cells': 0, '?': 0, #improved armored cells
                            'spread_spores': 0, 'longer_spore_range': 0, 'larger_spores': 0, #spore spreading ability
                            'ultimate?': 0} 
        
        else:
            self.tree = {'growth_buff': 0, 'defense_buff': 0, 'attack_buff': 0, #buffing poison
                             'slow_growth_poison': 0, 'no_growth_poison': 0, 'death_poison': 0, #area denial/attacking poison
                             'increased_exp_rate': 0, 'larger_exp_blast': 0, 'lingering_poison':0, #improving poison explosive cells
                             '': 0} #ultimate
            
    def update_tree(self, trait, value):
        self.tree[trait] = value

class SpriteKindDict:
    def __init__(self):
        super().__init__()
        
        self.sprite_dict = {'base_sprite': [(0,0,0), 0, 0, 0, [None]], 
                    'food_sprite': [(0,250,0), 0, 0, 0, [None]], 
                    'impass_sprite_1': [(75,50,50), 0, 1000, 0, [None]], 
                    'impass_sprite_2': [(75,50,55), 0, 1000, 0, [None]],
                    'slime_sprite_1': [(250,190,190), 30, 10, 0.025, ['slime_sprite_1', 'hyphae']], 
                    'slime_sprite_2': [(220,240,200), 30, 10, 0.025, ['slime_sprite_2', 'hyphae']],
                    'durable_sprite_1': [(120,180,100), 20, 20, 0.005, ['durable_sprite_1','armor_sprite_1', 'hyphae']], 
                    'durable_sprite_2': [(120,100,160), 20, 20, 0.005, ['durable_sprite_2','armor_sprite_2', 'hyphae']],
                    'poison_sprite_1': [(100,100,200), 15, 15, 0.0075, ['poison_sprite_1', 'exp_sprite_1', 'hyphae']], 
                    'poison_sprite_2': [(130,100,130), 15, 15, 0.0075, ['poison_sprite_2', 'exp_sprite_2', 'hyphae']],
                    'armor_sprite_1': [(50,100,50), 20, 30, 0.005, ['durable_sprite_1','armor_sprite_1', 'hyphae']], 
                    'armor_sprite_2': [(50,100,120), 20, 30, 0.005, ['durable_sprite_2','armor_sprite_2', 'hyphae']],
                    'exp_sprite_1': [(50,50,250), 0, 0, 0, ['poison_sprite_1', 'exp_sprite_1', 'hyphae']], 
                    'exp_sprite_2': [(230,50,230), 0, 0, 0, ['poison_sprite_2', 'exp_sprite_2', 'hyphae']]}
    
    def update_dict(self, sprite_kind, value):
        self.sprite_dict[sprite_kind] = value