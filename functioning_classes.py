import pygame
import random

clock = pygame.time.Clock()

global player1species
global player2species

global kind_sprite_dict 
kind_sprite_dict = {'base_sprite': [(0,0,0), 0, 0, 0, [None]], 
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


global sprite_dict
sprite_dict = {}

global trait_point_dict
trait_point_dict = {'1': 0, '2': 0}

global slime_mold_trait_dict_1
slime_mold_trait_dict_1 = {'splitting_cells': 0, 'plasmodium': 0, 'bouncing_plasmodium': 0,  #plasmodium abilities
                           'random_hyphae': 0, 'seeking_hyphae': 0,'food_hyphae': 0, '2_ai_hyphae': 0, #hyphae abilities
                           'faster_growth':0, 'stronger_attack': 0, 'exponential_growth': 0, #growth increase and EG ability
                           'pierching_hyphae': 0} #ultimate

global durable_fungi_trait_dict_1
durable_fungi_trait_dict_1 = {'short_tough_wall': 0, 'short_impenetrable_wall': 0, 'long_impenetrable_wall': 0, #defensive wall
                              'armored_cells_grow': 0, 'stronger_armored_cells': 0, '?': 0, #improved armored cells
                              'spread_spores': 0, 'longer_spore_range': 0, 'larger_spores': 0, #spore spreading ability
                              'ultimate?': 0} 

global poison_fungi_trait_dict_1
poison_fungi_trait_dict_1 = {'growth_buff': 0, 'defense_buff': 0, 'attack_buff': 0, #buffing poison
                             'slow_growth_poison': 0, 'no_growth_poison': 0, 'death_poison': 0, #area denial/attacking poison
                             'increased_exp_rate': 0, 'larger_exp_blast': 0, 'lingering_poison':0, #improving poison explosive cells
                             '': 0} #ultimate

global armor_cell_grow_1
armor_cell_grow_1 = False

global armor_cell_grow_2
armor_cell_grow_2 = False

###### Need to duplicate trait_dicts when finished!


#if example_dict['multiple_hyphae'] == 1:
#    y += 1

# All hyphae have:
# height
# width
# x loc
# y loc
# color

# All Hyphae can:
# move()
# return their loc

def updateTraitList(player_species, current_trait_list):
    None


class slimeHyphae(pygame.sprite.Sprite):
    def __init__(self, color, height, width, kind, paintkind):
        super().__init__()

        self.kind = kind
        self.paintkind = paintkind
        self.color = color
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        
        pygame.draw.rect(self.image,
                        color,
                        pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()  
    
    def paint_kind(self):
        if sprite_dict[self.rect.x, self.rect.y].kind == 'food_sprite':
            trait_point_dict[self.paintkind[-1:]] += 1
        sprite_dict[self.rect.x, self.rect.y].setKind(self.paintkind)
    
    def getLoc(self):
        return [self.rect.x, self.rect.y]

    def moveRight(self, pixels):
        self.rect.x += pixels
        self.paint_kind()
        if self.rect.x < world_dimensions[0] - 12:
            self.rect.x += pixels
            self.paint_kind()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        self.paint_kind()
        if self.rect.x > 2:
            self.rect.x -= pixels
            self.paint_kind()

    def moveUp(self, pixels):
        self.rect.y += pixels
        self.paint_kind()
        if self.rect.y < world_dimensions[1] - 12:
            self.rect.y += pixels
            self.paint_kind()

    def moveDown(self, pixels):
        self.rect.y -= pixels
        self.paint_kind()
        if self.rect.y > 2:
            self.rect.y -= pixels
            self.paint_kind()

    def moveUpLeft(self, pixels):
        self.rect.x -= pixels
        self.rect.y += pixels
        self.paint_kind()
        self.rect.x -= pixels
        self.rect.y += pixels
        self.paint_kind()

    def moveUpRight(self, pixels):
        self.rect.x += pixels
        self.rect.y += pixels
        self.paint_kind()
        self.rect.x += pixels
        self.rect.y += pixels
        self.paint_kind()

    def moveDownLeft(self, pixels):
        self.rect.y -= pixels
        self.rect.x -= pixels
        self.paint_kind()
        self.rect.y -= pixels
        self.rect.x -= pixels
        self.paint_kind()

    def moveDownRight(self, pixels):
        self.rect.y -= pixels
        self.rect.x += pixels
        self.paint_kind()
        self.rect.y -= pixels
        self.rect.x += pixels
        self.paint_kind()
    
class durableHyphae(pygame.sprite.Sprite):
    def __init__(self, color, height, width, kind, paintkind):
        super().__init__()

        self.kind = kind
        self.paintkind = paintkind
        self.color = color
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        
        pygame.draw.rect(self.image,
                        color,
                        pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()  
    
    def paint_kind(self):
        if sprite_dict[self.rect.x, self.rect.y].kind == 'food_sprite':
            trait_point_dict[self.paintkind[-1:]] += 1
        sprite_dict[self.rect.x, self.rect.y].setKind(self.paintkind)
    
    def getLoc(self):
        return [self.rect.x, self.rect.y]

    def moveRight(self, pixels):
        if sprite_dict[self.rect.x + pixels, self.rect.y].kind in [kind_sprite_dict[self.paintkind], 'base_sprite']:
            self.rect.x += pixels
            self.paint_kind()

    def moveLeft(self, pixels):
        if sprite_dict[self.rect.x - pixels, self.rect.y].kind in [self.paintkind, 'base_sprite']:
            self.rect.x -= pixels
            self.paint_kind()

    def moveUp(self, pixels):
        if sprite_dict[self.rect.x, self.rect.y + pixels].kind in [self.paintkind, 'base_sprite']:
            self.rect.y += pixels
            self.paint_kind()

    def moveDown(self, pixels):
        if sprite_dict[self.rect.x, self.rect.y - pixels].kind in [self.paintkind, 'base_sprite']:
            self.rect.y -= pixels
            self.paint_kind()

    def moveUpLeft(self, pixels):
        if sprite_dict[self.rect.x - pixels, self.rect.y + pixels].kind in [self.paintkind, 'base_sprite']:
            self.rect.x -= pixels
            self.rect.y += pixels
            self.paint_kind()

    def moveUpRight(self, pixels):
        if sprite_dict[self.rect.x + pixels, self.rect.y + pixels].kind in [self.paintkind, 'base_sprite']:
            self.rect.x += pixels
            self.rect.y += pixels
            self.paint_kind()

    def moveDownLeft(self, pixels):
        if sprite_dict[self.rect.x - pixels, self.rect.y - pixels].kind in [self.paintkind, 'base_sprite']:
            self.rect.y -= pixels
            self.rect.x -= pixels
            self.paint_kind()

    def moveDownRight(self, pixels):
        if sprite_dict[self.rect.x + pixels, self.rect.y - pixels].kind in [self.paintkind, 'base_sprite']:
            self.rect.y -= pixels
            self.rect.x += pixels
            self.paint_kind()

class poisonHyphae(pygame.sprite.Sprite):
    def __init__(self, color, height, width, kind, paintkind):
        super().__init__()

        self.kind = kind
        self.paintkind = paintkind
        self.color = color
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        
        pygame.draw.rect(self.image,
                        color,
                        pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()  
    
    def paint_kind(self):
        if sprite_dict[self.rect.x, self.rect.y].kind == 'food_sprite':
            trait_point_dict[self.paintkind[0][-1:]] += 1
        if sprite_dict[self.rect.x, self.rect.y].kind == 'exp_sprite_1' or sprite_dict[self.rect.x, self.rect.y].kind == 'exp_sprite_2':
            None
        else:
            if random.random() < 0.75:
                sprite_dict[self.rect.x, self.rect.y].setKind(self.paintkind[0])
            else:
                sprite_dict[self.rect.x, self.rect.y].setKind(self.paintkind[1])

    def getLoc(self):
        return [self.rect.x, self.rect.y]

    def moveRight(self, pixels):
        if sprite_dict[self.rect.x + pixels, self.rect.y].kind in [self.paintkind[0], self.paintkind[1], 'base_sprite']:
            self.rect.x += pixels
            self.paint_kind()

    def moveLeft(self, pixels):
        if sprite_dict[self.rect.x - pixels, self.rect.y].kind in [self.paintkind[0], self.paintkind[1], 'base_sprite']:
            self.rect.x -= pixels
            self.paint_kind()

    def moveUp(self, pixels):
        if sprite_dict[self.rect.x, self.rect.y + pixels].kind in [self.paintkind[0], self.paintkind[1], 'base_sprite']:
            self.rect.y += pixels
            self.paint_kind()

    def moveDown(self, pixels):
        if sprite_dict[self.rect.x, self.rect.y - pixels].kind in [self.paintkind[0], self.paintkind[1], 'base_sprite']:
            self.rect.y -= pixels
            self.paint_kind()

    def moveUpLeft(self, pixels):
        if sprite_dict[self.rect.x - pixels, self.rect.y + pixels].kind in [self.paintkind[0], self.paintkind[1], 'base_sprite']:
            self.rect.x -= pixels
            self.rect.y += pixels
            self.paint_kind()

    def moveUpRight(self, pixels):
        if sprite_dict[self.rect.x + pixels, self.rect.y + pixels].kind in [self.paintkind[0], self.paintkind[1], 'base_sprite']:
            self.rect.x += pixels
            self.rect.y += pixels
            self.paint_kind()

    def moveDownLeft(self, pixels):
        if sprite_dict[self.rect.x - pixels, self.rect.y - pixels].kind in [self.paintkind[0], self.paintkind[1], 'base_sprite']:
            self.rect.y -= pixels
            self.rect.x -= pixels
            self.paint_kind()

    def moveDownRight(self, pixels):
        if sprite_dict[self.rect.x + pixels, self.rect.y - pixels].kind in [self.paintkind[0], self.paintkind[1], 'base_sprite']:
            self.rect.y -= pixels
            self.rect.x += pixels
            self.paint_kind()

class Sprite(pygame.sprite.Sprite):
    def __init__(self, height, width, x_loc, y_loc, kind):
        super().__init__()
        self.kind = kind
        self.color, self.attack_val, self.defense_val, self.growth_rate, self.dont_grow_list = self.getAttributes(kind)

        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        
        self.rect = self.image.get_rect()

        self.rect.x = x_loc
        self.rect.y = y_loc

        pygame.draw.rect(self.image, self.color,
                        pygame.Rect(0, 0, width, height))
    
    def setKind(self, new_kind):
        if self.kind == 'exp_sprite_1' or self.kind == 'exp_sprite_2':
            exp_dont_kill_list = self.dont_grow_list
            
            growth_list = []
            self.kind = 'base_sprite'
            self.color, self.attack_val, self.defense_val, self.growth_rate, self.dont_grow_list = self.getAttributes(self.kind)
            for i in [-48, -36, -24, -12, 0, 12, 24, 36, 48]:
                for j in [-48, -36, -24, -12, 0, 12, 24, 36, 48]:
                    if (self.rect.x + i > 0 and self.rect.x + i < world_dimensions[0]) and (self.rect.y + j > 0 and self.rect.y + j < world_dimensions[1]):
                        growth_list.append((self.rect.x + i, self.rect.y + j))
            #print(growth_list)
            for loc in growth_list:
                example_sprite = sprite_dict[loc]
                if str(example_sprite.kind) in exp_dont_kill_list:
                    None
                else:
                    example_sprite.setKind('base_sprite')

        # Need to fix above code ^
        else:
            self.kind = new_kind
            self.color, self.attack_val, self.defense_val, self.growth_rate, self.dont_grow_list = self.getAttributes(self.kind)
        pygame.draw.rect(self.image, self.color,
                            pygame.Rect(0, 0, self.width, self.height))

    def getAttributes(self, kind):   
        return kind_sprite_dict[kind]
    
    def grow(self):
        if self.growth_rate == 0:
            return
        else:
            growth_list = []
            for i in [-12, 0, 12]:
                for j in [-12, 0, 12]:
                    if (self.rect.x + i > 0 and self.rect.x + i < world_dimensions[0]) and (self.rect.y + j > 0 and self.rect.y + j < world_dimensions[1]):
                        growth_list.append((self.rect.x + i, self.rect.y + j))
            growth_counter = 0
            for loc in growth_list:
                example_sprite = sprite_dict[loc]
                if example_sprite.kind in self.dont_grow_list:
                    growth_counter += 1
                else:
                    #armor_cell_grow_1 = True
                    if self.attack_val > example_sprite.defense_val and random.random() < self.growth_rate:
                        if example_sprite.kind == 'food_sprite':
                            trait_point_dict[self.kind[-1:]] += 1
                        if self.kind == 'armor_sprite_1' and armor_cell_grow_1 != True:
                            example_sprite.setKind('durable_sprite_1')    
                        elif self.kind == 'armor_sprite_2'and armor_cell_grow_1 != True:
                            example_sprite.setKind('durable_sprite_2')
                        else:
                            example_sprite.setKind(self.kind)
            if growth_counter == 9:
                self.growth_rate = 0                             
                                
def updateSprites():
    cell_list = list(range(0,len(all_sprites_list)))
    for i in range(len(all_sprites_list)):
        x = random.choice(cell_list)
        cell_list.remove(x)
        example_sprite = all_sprites_list.sprites()[x]
        if example_sprite.kind != 'hyphae':
            example_sprite.grow()

def moveHyphae(P1Hyphae, P2Hyphae):
    keys = pygame.key.get_pressed()                    
    if keys[pygame.K_LEFT] and P1Hyphae.rect.x > 2:
        P1Hyphae.moveLeft(12)
    if keys[pygame.K_RIGHT] and P1Hyphae.rect.x < world_dimensions[0] - 12:
        P1Hyphae.moveRight(12)
    if keys[pygame.K_DOWN] and P1Hyphae.rect.y < world_dimensions[1] - 12:
        P1Hyphae.moveUp(12)
    if keys[pygame.K_UP]  and P1Hyphae.rect.y > 2:
        P1Hyphae.moveDown(12)

    if keys[pygame.K_a] and P2Hyphae.rect.x > 2:
        P2Hyphae.moveLeft(12)
    if keys[pygame.K_d] and P2Hyphae.rect.x < world_dimensions[0] - 12:
        P2Hyphae.moveRight(12)
    if keys[pygame.K_s] and P2Hyphae.rect.y < world_dimensions[1] - 12:
        P2Hyphae.moveUp(12)
    if keys[pygame.K_w]  and P2Hyphae.rect.y > 2:
        P2Hyphae.moveDown(12)

def generateWorld(world_dimensions, player1species, player2species):
    #Colors
    BLACK = (0,0,0)
    RED = (255,100,0)
    BLUE = (0, 0, 255)
    ORANGE = (255, 100, 0)
    GREEN =  (0, 200, 200)
    TRUEGREEN = (0, 255, 0)
    DARKGREEN = (0, 200, 100)
    PURPLE = (128, 0, 128)
    trait_point_dict = {RED: 0, BLUE: 0, GREEN: 0, DARKGREEN: 0}
    # World Options
    world_color = (200,200,200)
    sprite_size = [10, 10]
    
    if player1species == 0:
        P1Hyphae = durableHyphae(GREEN, sprite_size[0], sprite_size[1], 'hyphae', 'armor_sprite_1')
    
    if player1species == 1:
        P1Hyphae = slimeHyphae(RED, sprite_size[0], sprite_size[1], 'hyphae', 'slime_sprite_1')

    if player1species == 2:
        P1Hyphae = poisonHyphae(PURPLE, sprite_size[0], sprite_size[1], 'hyphae', ['poison_sprite_1', 'exp_sprite_1'])

    if player2species == 0:
        P2Hyphae = durableHyphae(GREEN, sprite_size[0], sprite_size[1], 'hyphae', 'armor_sprite_2')
    
    if player2species == 1:
        P2Hyphae = slimeHyphae(RED, sprite_size[0], sprite_size[1], 'hyphae', 'slime_sprite_2')

    if player2species == 2:
        P2Hyphae = poisonHyphae(PURPLE, sprite_size[0], sprite_size[1], 'hyphae', ['poison_sprite_2', 'exp_sprite_2'])

    
    food_rate = 0.01

    sample_surface = pygame.display.set_mode((world_dimensions[0], world_dimensions[1]))
    sample_surface.fill((200,200,200))
    all_sprites_list = pygame.sprite.Group()

    for i in range(2, world_dimensions[0]-6, 12):
        for j in range(2, world_dimensions[1]-6, 12):
            if random.random() > 0.99:
                y = Sprite(sprite_size[0], sprite_size[1], i, j, 'food_sprite')
            else:
                y = Sprite(sprite_size[0], sprite_size[1], i, j, 'base_sprite')
            all_sprites_list.add(y)
            sprite_dict.update({(y.rect[0], y.rect[1]): y})

    P1Hyphae.rect.x = 470
    P1Hyphae.rect.y = 470

    P2Hyphae.rect.x = 26
    P2Hyphae.rect.y = 26

    sprite1 = sprite_dict[470,470]      

    sprite2 = sprite_dict[26,26]      

    if player1species == 0:
        sprite1.setKind('durable_sprite_1')

    if player1species == 1:
        sprite1.setKind('slime_sprite_1')

    if player1species == 2:
        sprite1.setKind('poison_sprite_1')

    if player2species == 0:
        sprite2.setKind('durable_sprite_2')

    if player2species == 1:
        sprite2.setKind('slime_sprite_2')

    if player2species == 2:
        sprite2.setKind('poison_sprite_2')

    all_sprites_list.add(sprite1)
    all_sprites_list.add(P1Hyphae)
    all_sprites_list.add(sprite2)
    all_sprites_list.add(P2Hyphae)
    pygame.init()

    return all_sprites_list, sample_surface, P1Hyphae, P2Hyphae

count = 0
exit = False
world_dimensions = [506, 506] #506

all_sprites_list, sample_surface, P1Hyphae, P2Hyphae = generateWorld(world_dimensions, player1species = 2, player2species = 0)

while not exit:
    all_sprites_list.update()
    all_sprites_list.draw(sample_surface)
    pygame.display.flip()

    #print(trait_point_dict)

    updateSprites()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit = True
    
    moveHyphae(P1Hyphae, P2Hyphae)

    all_sprites_list.update()
    all_sprites_list.draw(sample_surface)
    
    pygame.display.flip()
    
    clock.tick(15)
    #print(count)
    count += 1 

### If you are a normal sprite you make more sprites of your own kind
# if you are are a sprite and you are next to another sprite and you want to grow you compare your attack to their defense
# if you have a higher att than they have defense you can grow on top of them thereby killing them and producing another sprite

# sprites have:
# height
# width
# x loc
# y loc
# color
# attack
# defense
# kind

# sprites can:
# grow()


# kinds of sprites:
# - Base sprites (no att or def)
kind = 'base_sprite'
# - Impassable/unkillable sprites
kind = 'impass_sprite_1'
kind = 'impass_sprite_2'
# - slime sprites
kind = 'slime_sprite_1'
kind = 'slime_sprite_2'
# - durable sprites
kind = 'durable_sprite_1'
kind = 'durable_sprite_2'
# - poison sprites
kind = 'poison_sprite_1'
kind = 'poison_sprite_2'
# - armor sprites
kind = 'armor_sprite_1'
kind = 'armor_sprite_2'
# - explosive sprites
kind = 'exp_sprite_1'
kind = 'exp_sprite_2'

### If you are a hyphae you leave behind sprites, in the case of durable hyphae and poison hyphae you leave behind special sprites
# As a hyphae you cannot move on top of enemy sprites unless you have the Piercing Hyphae feature of slime molds

# All hyphae have:
# height
# width
# x loc
# y loc
# color

# All Hyphae can:
# move()
# return their loc

# Slime hyphae can

