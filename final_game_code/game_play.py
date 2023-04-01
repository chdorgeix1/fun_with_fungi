# this file will be the final game file that combines all of the other files

import pygame
import hyphae_classes



import game_dicts

player_1_trait_dict = game_dicts.slime_mold_trait_dict

player_2_trait_dict = game_dicts.slime_mold_trait_dict

player_1_trait_dict['splitting_cells'] = 1

print(player_1_trait_dict['splitting_cells'])
print(player_2_trait_dict['splitting_cells'])

#p1Hyphae = hyphae_classes.slimeHyphae((255,0,0), 20, 20, 'bug', 'bugs1')

#p1Hyphae.paint_kind()