# this file contains the species trait trees

from dataclasses import dataclass

@dataclass
class DurableTraitTree():
    short_tough_wall: int = 0
    short_impenetrable_wall: int = 0
    long_impenetrable_wall: int = 0 #defensive wall
    armored_cells_grow: int = 0
    stronger_armored_cells: int = 0
    final_armor_cell_buff: int = 0 #improved armored cells
    spread_spores: int = 0
    longer_spore_range: int = 0
    larger_spores: int = 0 #spore spreading ability
    ultimate_undetermined: int = 0 


@dataclass
class PoisonTraitTree():
    growth_buff: int = 0
    defense_buff: int = 0
    attack_buff: int = 0 #buffing poison
    slow_growth_poison: int = 0
    no_growth_poison: int = 0
    death_poison: int = 0 #area denial/attacking poison
    increased_exp_rate: int = 0
    larger_exp_blast: int = 0
    lingering_poison: int = 0 #improving poison explosive cells
    undetermined_ultimate: int = 0 #ultimate

@dataclass
class SlimeTraitTree():
    splitting_cells: int = 0
    plasmodium: int = 0
    bouncing_plasmodium: int = 0  #plasmodium abilities
    random_hyphae: int = 0
    seeking_hyphae: int = 0
    food_hyphae: int = 0
    double_ai_hyphae:  int = 0, #hyphae abilities
    faster_growth: int = 0
    stronger_attack: int = 0,
    exponential_growth: int = 0 #growth increase and EG ability
    pierching_hyphae: int = 0 #ultimate
   