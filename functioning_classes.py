import pygame
import random

clock = pygame.time.Clock()

global player1species
global player2species

global kind_sprite_dict 
kind_sprite_dict = {'base_sprite': [(0,0,0), 0, 0, 0, [None]], 
                    'impass_sprite_1': [(75,50,50), 0, 1000, 0, [None]], 
                    'impass_sprite_2': [(75,50,55), 0, 1000, 0, [None]],
                    'slime_sprite_1': [(250,190,190), 10, 10, 0.1, ['slime_sprite_1', 'exp_sprite_1', 'hyphae']], 
                    'slime_sprite_2': [(220,240,200), 10, 10, 0.1, ['slime_sprite_2', 'exp_sprite_2', 'hyphae']],
                    'durable_sprite_1': [(120,180,100), 20, 20, 0.05, ['durable_sprite_1','armor_sprite_1', 'hyphae']], 
                    'durable_sprite_2': [(120,100,160), 20, 20, 0.05, ['durable_sprite_2','armor_sprite_2', 'hyphae']],
                    'poison_sprite_1': [(100,100,200), 15, 15, 0.075, ['poison_sprite_1', 'exp_sprite_1', 'hyphae']], 
                    'poison_sprite_2': [(130,100,130), 15, 15, 0.075, ['poison_sprite_2', 'exp_sprite_2', 'hyphae']],
                    'armor_sprite_1': [(50,100,50), 0, 30, 0.05, ['durable_sprite_1','armor_sprite_1', 'hyphae']], 
                    'armor_sprite_2': [(50,50,120), 0, 30, 0.05, ['durable_sprite_2','armor_sprite_2', 'hyphae']],
                    'exp_sprite_1': [(50,50,250), 0, 0, 0, [None]], 
                    'exp_sprite_2': [(230,50,230), 0, 0, 0, [None]]}

global sprite_dict
sprite_dict = {}

# All hyphae have:
# height
# width
# x loc
# y loc
# color

# All Hyphae can:
# move()
# return their loc

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
        sprite_dict[self.rect.x, self.rect.y].setKind(self.paintkind)
    
    def getLoc(self):
        return [self.rect.x, self.rect.y]

    def moveRight(self, pixels):
        self.rect.x += pixels
        self.paint_kind()
        pygame.draw.rect(sample_surface, self.color,
                                pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        self.paint_kind()

    def moveUp(self, pixels):
        self.rect.y += pixels
        self.paint_kind()

    def moveDown(self, pixels):
        self.rect.y -= pixels
        self.paint_kind()

    def moveUpLeft(self, pixels):
        self.rect.x -= pixels
        self.rect.y += pixels
        self.paint_kind()

    def moveUpRight(self, pixels):
        self.rect.x += pixels
        self.rect.y += pixels
        self.paint_kind()

    def moveDownLeft(self, pixels):
        self.rect.y -= pixels
        self.rect.x -= pixels
        self.paint_kind()

    def moveDownRight(self, pixels):
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
                    if self.attack_val > example_sprite.defense_val and  random.random() > 1:#random.random() < self.growth_rate:
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

def moveHyphae(P1Hyphae, P2Hyphae = None):
    keys = pygame.key.get_pressed()                    
    if keys[pygame.K_LEFT] and P1Hyphae.rect.x > 2:
        P1Hyphae.moveLeft(12)
    if keys[pygame.K_RIGHT] and P1Hyphae.rect.x < world_dimensions[0] - 22:
        P1Hyphae.moveRight(12)
    if keys[pygame.K_DOWN] and P1Hyphae.rect.y < world_dimensions[1] - 22:
        P1Hyphae.moveUp(12)
    if keys[pygame.K_UP]  and P1Hyphae.rect.y > 2:
        P1Hyphae.moveDown(12)


def generateWorld(world_dimensions, player1species, player2species = None):
    #Colors
    BLACK = (0,0,0)
    RED = (255,100,0)
    BLUE = (0, 0, 255)
    ORANGE = (255, 100, 0)
    GREEN =  (0, 200, 200)
    TRUEGREEN = (0, 255, 0)
    DARKGREEN = (0, 200, 100)
    trait_point_dict = {RED: 0, BLUE: 0, GREEN: 0, DARKGREEN: 0}
    # World Options
    world_color = (200,200,200)
    sprite_size = [10, 10]

    if player1species == 1:
        P1Hyphae = slimeHyphae(RED, sprite_size[0], sprite_size[1], 'hyphae', 'slime_sprite_1')

    
    food_rate = 0.01

    sample_surface = pygame.display.set_mode((world_dimensions[0], world_dimensions[1]))
    sample_surface.fill((200,200,200))
    all_sprites_list = pygame.sprite.Group()

    for i in range(2, world_dimensions[0]-6, 12):
        for j in range(2, world_dimensions[1]-6, 12):
            y = Sprite(sprite_size[0], sprite_size[1], i, j, 'base_sprite')
            all_sprites_list.add(y)
            sprite_dict.update({(y.rect[0], y.rect[1]): y})
    
    P1Hyphae.rect.x = 26
    P1Hyphae.rect.y = 26

    sprite1 = sprite_dict[26,26]      
    sprite1.setKind('slime_sprite_1')

    all_sprites_list.add(sprite1)
    all_sprites_list.add(P1Hyphae)
    pygame.init()

    return all_sprites_list, sample_surface, P1Hyphae

count = 0
exit = False
world_dimensions = [506, 506]

all_sprites_list, sample_surface, P1Hyphae = generateWorld(world_dimensions, player1species = 1)

while not exit:
    all_sprites_list.update()
    all_sprites_list.draw(sample_surface)
    pygame.display.flip()

    updateSprites()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit = True
    
    moveHyphae(P1Hyphae)

    all_sprites_list.update()
    all_sprites_list.draw(sample_surface)
    
    pygame.display.flip()
    
    clock.tick(100)
    print(count)
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

