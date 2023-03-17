# import pygame package
import pygame
import pygame_menu
import random

def testMain():
    def set_player_class(value):
        if value == 1:
            return 'hamsters'
    def designWorld(player_class = 0, ai_class = 0, difficulty = 0, world_map = 0):
        
        # Code fplayers to choose their class
        player_class_choice = set_player_class(player_class)
        # Code for players to choose ai_class
        #ai_class_choice = 
        # Code for players to set difficulty
        difficulty = 4
        # Code for world map_choice
        map_choice = 0

        return (player_class_choice, ai_class_choice, difficulty, map_choice)

    def createWorld(sample_surface, world_dimensions, world_color, food_rate = 0.01):
        sample_surface.fill(world_color)

        #World Generation
        food_count = 0
        for i in range(2, world_dimensions[0]-6, 12):
            for j in range(2, world_dimensions[1]-6, 12):
                if random.random() > 1 - food_rate:
                    y = Sprite(TRUEGREEN, sprite_size[0], sprite_size[1], i, j)
                    food_sprite_list.add(y)
                    food_count += 1
                else:
                    y = Sprite(BLACK, sprite_size[0], sprite_size[1], i, j)
                all_sprites_list.add(y)
        print(food_count)
        playerHyphae = Hyphae(ORANGE, RED, 10, 10)
        playerHyphae.rect.x = 470
        playerHyphae.rect.y = 470

        playerHyphae1 = Hyphae(GREEN, BLUE, 10, 10)
        playerHyphae1.rect.x = 26
        playerHyphae1.rect.y = 26
        
        all_sprites_list.add(playerHyphae)
        all_sprites_list.add(playerHyphae1)

        playerHyphae = Hyphae(ORANGE, RED, 10, 10)
        playerHyphae.rect.x = 470
        playerHyphae.rect.y = 470

        playerHyphae1 = Hyphae(GREEN, BLUE, 10, 10)
        playerHyphae1.rect.x = 26
        playerHyphae1.rect.y = 26
        
        all_sprites_list.add(playerHyphae)
        all_sprites_list.add(playerHyphae1)

        sprite_dict = {}
        for ex_sprite in all_sprites_list:
            sprite_dict.update({(ex_sprite.rect[0], ex_sprite.rect[1]): ex_sprite})
        
        red_sprites_list.add(sprite_dict[(world_dimensions[0]-12,world_dimensions[1]-12)])
        blue_sprites_list.add(sprite_dict[(2,2)]) 

        red_sprites_list.add(playerHyphae)
        return clock, sample_surface, all_sprites_list, food_sprite_list, red_sprites_list, blue_sprites_list, sprite_dict, playerHyphae, playerHyphae1


    def generateWorld(world_color, world_dimensions, sprite_size, food_rate = 0.01):
        # World set up and iniation
        clock = pygame.time.Clock()

        #world_color = (200,200,200)
        #world_dimensions = [506, 506]
        #sprite_size = [10, 10]
        sample_surface = pygame.display.set_mode((world_dimensions[0],world_dimensions[1]))
        
        sample_surface.fill(world_color)

        #Sprite lists probably need a hyphae group and nonhyphae groups
        all_sprites_list = pygame.sprite.Group()
        red_sprites_list = pygame.sprite.Group()
        blue_sprites_list = pygame.sprite.Group()
        food_sprite_list = pygame.sprite.Group()

        #World Generation
        food_count = 0
        for i in range(2, world_dimensions[0]-6, 12):
            for j in range(2, world_dimensions[1]-6, 12):
                if random.random() > 1 - food_rate:
                    y = Sprite(TRUEGREEN, sprite_size[0], sprite_size[1], i, j)
                    food_sprite_list.add(y)
                    food_count += 1
                else:
                    y = Sprite(BLACK, sprite_size[0], sprite_size[1], i, j)
                all_sprites_list.add(y)
        print(food_count)
        playerHyphae = Hyphae(ORANGE, RED, 10, 10)
        playerHyphae.rect.x = 470
        playerHyphae.rect.y = 470

        playerHyphae1 = Hyphae(GREEN, BLUE, 10, 10)
        playerHyphae1.rect.x = 26
        playerHyphae1.rect.y = 26
        
        all_sprites_list.add(playerHyphae)
        all_sprites_list.add(playerHyphae1)

        sprite_dict = {}
        for ex_sprite in all_sprites_list:
            sprite_dict.update({(ex_sprite.rect[0], ex_sprite.rect[1]): ex_sprite})
        
        red_sprites_list.add(sprite_dict[(world_dimensions[0]-12,world_dimensions[1]-12)])
        blue_sprites_list.add(sprite_dict[(2,2)]) 

        red_sprites_list.add(playerHyphae)
        return clock, sample_surface, all_sprites_list, food_sprite_list, red_sprites_list, blue_sprites_list, sprite_dict, playerHyphae, playerHyphae1

    def traitUpgrade():
        print('')


    # The Hyphae class is a sprite that users can move to spread their growth around the world
    class Hyphae(pygame.sprite.Sprite):
        def __init__(self, color, trail, height, width):
            super().__init__()

            self.color = color
            self.trail = trail
            self.width = width
            self.height = height
            self.image = pygame.Surface([width, height])
            
            pygame.draw.rect(self.image,
                            color,
                            pygame.Rect(0, 0, width, height))

            self.rect = self.image.get_rect()    

        def getColors(self):
            return [self.color, self.trail]

        def getX(self):
            return self.rect.x
        
        def getY(self):
            return self.rect.y
        
        def moveRight(self, pixels):
            pygame.draw.rect(sample_surface, self.trail,
                            pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
            self.rect.x += pixels

        def moveLeft(self, pixels):
            pygame.draw.rect(sample_surface, self.trail,
                            pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
            self.rect.x -= pixels

        def moveUp(self, pixels):
            pygame.draw.rect(sample_surface, self.trail,
                            pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
            self.rect.y += pixels

        def moveDown(self, pixels):
            pygame.draw.rect(sample_surface, self.trail,
                            pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
            self.rect.y -= pixels

        def moveUpLeft(self, pixels):
            pygame.draw.rect(sample_surface, self.trail,
                            pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
            self.rect.x -= pixels
            self.rect.y += pixels

        def moveUpRight(self, pixels):
            pygame.draw.rect(sample_surface, self.trail,
                            pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
            self.rect.x += pixels
            self.rect.y += pixels

        def moveDownLeft(self, pixels):
            pygame.draw.rect(sample_surface, self.trail,
                            pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
            self.rect.y -= pixels
            self.rect.x -= pixels

        def moveDownRight(self, pixels):
            pygame.draw.rect(sample_surface, self.trail,
                            pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
            self.rect.y -= pixels
            self.rect.x += pixels
        
        def paintSprites(self,group):
            for example_sprite in all_sprites_list:
                if example_sprite != playerHyphae or example_sprite != playerHyphae1:
                    if example_sprite.rect[0:2] == self.rect[0:2]:
                        if example_sprite in food_sprite_list:
                            trait_point_dict[self.trail] += 1
                        example_sprite.kill()
                        group.add(example_sprite)
                        all_sprites_list.add(example_sprite)


    # The sprite class is both the world the player's hyphae move on and can become of the player's sprite list
    # Sprites in a sprite list "grow" or spread their sprite list to other nearby sprites 

    class Sprite(pygame.sprite.Sprite):
        def __init__(self, color, height, width, x_loc, y_loc, growing = True):
            super().__init__()

            self.growth_state = growing
            self.color = color
            self.width = width
            self.height = height
            self.image = pygame.Surface([width, height])
            
            self.rect = self.image.get_rect()

            self.rect.x = x_loc
            self.rect.y = y_loc

            pygame.draw.rect(self.image, color,
                            pygame.Rect(0, 0, width, height))
            
        def changeColor(self, new_color):
            self.color = new_color
            pygame.draw.rect(self.image, self.color,
                                pygame.Rect(0, 0, self.width, self.height))
        
        def naturalGrowth(self, group, growth_count = 0, growthmod = 0, fillrate = 0):
            if self.growth_state == True:
                growth_list = []
                for i in [-12, 0, 12]:
                    for j in [-12, 0, 12]:
                        if (self.rect.x + i > 0 and self.rect.x + i < world_dimensions[0]) and (self.rect.y + j > 0 and self.rect.y + j < world_dimensions[1]):
                            growth_list.append((self.rect.x + i, self.rect.y + j))
                growth_counter = 0
                for loc in growth_list:
                    example_sprite = sprite_dict[loc]
                    if example_sprite.color == self.color:
                        growth_counter += 1
                    else:
                        if random.random() > 1 - growthmod:
                            if example_sprite in food_sprite_list:
                                trait_point_dict[self.color] += 1
                            example_sprite.kill()
                            group.add(example_sprite)
                            all_sprites_list.add(example_sprite)
                if growth_counter >= 9 - growth_count:
                    self.growth_state = False
            else:
                if random.random() > 1 - fillrate:
                    self.growth_state = True
    
    # Behavior of sprites in the blue_sprite_list, this list will eventually be swapped/renamed to a type of fungi/slime mold
    # This behavior includes removal of sprite from other lists, growth, 
    def blueSpriteBehavior(blue_sprite, values):
        growth_count, growthmod, fillrate = values[0], values[1], values[2]
        if len(blue_sprite.groups()) > 2:
            blue_sprite.remove(red_sprites_list)
        if blue_sprite != playerHyphae and blue_sprite != playerHyphae1:
            blue_sprite.changeColor(BLUE)
            blue_sprite.naturalGrowth(blue_sprites_list, growth_count, growthmod, fillrate)
    
    def redSpriteBehavior(red_sprite, values):
        growth_count, growthmod, fillrate = values[0], values[1], values[2]
        if len(red_sprite.groups()) > 2:
            red_sprite.remove(blue_sprites_list)
        if red_sprite != playerHyphae and red_sprite != playerHyphae1:
            red_sprite.changeColor(RED)
            red_sprite.naturalGrowth(red_sprites_list, growth_count, growthmod, fillrate)



    #Colors
    BLACK = (0,0,0)
    RED = (255,0,0)
    BLUE = (0, 0, 255)
    ORANGE = (255, 100, 0)
    GREEN =  (0, 200, 200)
    TRUEGREEN = (0, 255, 0)
    trait_point_dict = {RED: 0, BLUE: 0}
    # World Options
    world_color = (200,200,200)
    world_dimensions = [506, 506]
    sprite_size = [10, 10]
    food_rate = 0.01

    blue_sprite_values = [3, 0.01, 0.1]
    red_sprites_values = [3, 0.01, 0.1]
    

    
    (clock, sample_surface, all_sprites_list, food_sprite_list, red_sprites_list, blue_sprites_list, 
    sprite_dict, playerHyphae, playerHyphae1) = generateWorld(world_color, world_dimensions, sprite_size, food_rate)
    playerHyphae.paintSprites(red_sprites_list)
    playerHyphae1.paintSprites(blue_sprites_list)


    #widget = menu.get_widget('test_widget')
    #selected = menu.get_selected_widget()

    def beginGame():
        count = 0
        exit = False
        while not exit:
            paused = False
            for event in pygame.event.get():
                #print('here')
                if event.type == pygame.QUIT:
                    exit = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        exit = True
                    if event.key == pygame.K_p: # Pausing
                        #print('here1')
                        paused = True
                        while paused:
                            pygame.time.delay(10)
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_u:  # Unpausing
                                        paused = False
                    #if event.key == pygame.K_y:


            if not paused:
                if trait_point_dict[RED] == 1:
                    print('Increased GROWTH')
                    red_sprites_values[1] += 0.1
                count += 1
                print(trait_point_dict)
                cell_list = list(range(0,len(all_sprites_list)))
                for i in range(len(all_sprites_list)):
                    x = random.choice(cell_list)
                    cell_list.remove(x)
                    example_sprite = all_sprites_list.sprites()[x]
                    if example_sprite in red_sprites_list:
                        redSpriteBehavior(example_sprite, red_sprites_values)
                    if example_sprite in blue_sprites_list:
                        blueSpriteBehavior(example_sprite, blue_sprite_values)
                        
                count_list = list(range(0,1000,50))
                if count in count_list:
                    print('')
                    print('Number of blue sprites:')
                    print(len(blue_sprites_list.sprites()))
                    print('Number of red sprites:')
                    print(len(red_sprites_list.sprites()))
                    print('')
                    print('')
                    print('')

                
                keys = pygame.key.get_pressed()                    
                if keys[pygame.K_LEFT] and playerHyphae.rect.x > 2:
                    playerHyphae.moveLeft(12)
                    playerHyphae.paintSprites(red_sprites_list)
                if keys[pygame.K_RIGHT] and playerHyphae.rect.x < world_dimensions[0] - 22:
                    playerHyphae.moveRight(12)
                    playerHyphae.paintSprites(red_sprites_list)
                if keys[pygame.K_DOWN] and playerHyphae.rect.y < world_dimensions[1] - 22:
                    playerHyphae.moveUp(12)
                    playerHyphae.paintSprites(red_sprites_list)
                if keys[pygame.K_UP]  and playerHyphae.rect.y > 2:
                    playerHyphae.moveDown(12)
                    playerHyphae.paintSprites(red_sprites_list)
                
                if playerHyphae1 in all_sprites_list:
                    keys2 = pygame.key.get_pressed()
                    if keys2[pygame.K_a] and playerHyphae1.rect.x > 2:
                        playerHyphae1.moveLeft(12)
                        playerHyphae1.paintSprites(blue_sprites_list)
                    if keys2[pygame.K_d] and playerHyphae1.rect.x < world_dimensions[0] - 22:
                        playerHyphae1.moveRight(12)
                        playerHyphae1.paintSprites(blue_sprites_list)
                    if keys2[pygame.K_s] and playerHyphae1.rect.y < world_dimensions[1] - 22:
                        playerHyphae1.moveUp(12)
                        playerHyphae1.paintSprites(blue_sprites_list)
                    if keys2[pygame.K_w]  and playerHyphae1.rect.y > 2:
                        playerHyphae1.moveDown(12)
                        playerHyphae1.paintSprites(blue_sprites_list)

                all_sprites_list.update()

                all_sprites_list.draw(sample_surface)
                pygame.display.flip()
                clock.tick(5)
                #clock.tick(2)

    def set_difficulty(value, difficulty):
        while True:
            print(value, difficulty)

    # def start():
    #     pygame.init()
    #     surface = pygame.display.set_mode((500,500))
    #     menu = pygame_menu.Menu('Welcome', 500, 500, theme = pygame_menu.themes.THEME_BLUE)
    #     menu.add.text_input('Name:')
    #     #x = menu.add.selector('Difficulty:', [('HARD', 1), ('EASY', 2)], onchange = x.get_value())
    #     #y = x.get_value()
    #     #print(y)
    #     #menu.add.button('Play', beginGame())

    #     menu.mainloop(surface)
    #     #menu.mainloop(surface)

    # start()
    beginGame()
    

    pygame.quit()

testMain()













def Main3():
    # GLOBAL VARIABLES
    #COLOR = (255, 100, 98)
    #SURFACE_COLOR = (167, 255, 100)
    #WIDTH = 500
    #HEIGHT = 500
    cube_size = 20
    line_width = 2
    range_gap = cube_size + line_width
    world_color = (0,0,0)
    
    num_cubes = 20
    num_lines = num_cubes + 1 #is one more than # cubes
    
    display_size = num_cubes * cube_size + num_lines * line_width # display_size = x(line_width) + y(cube_size), x = y+1 (one more line than cube)

    sample_surface = pygame.display.set_mode((display_size,display_size))
    
    sample_surface.fill((200, 200, 200))

    for i in range(0, display_size, range_gap):
        for j in range(0, display_size, range_gap):
            # Drawing Rectangle
            pygame.draw.rect(sample_surface, world_color,
                            pygame.Rect(i + line_width, j + line_width, cube_size, cube_size))

    # Object class
    class Sprite(pygame.sprite.Sprite):
        def __init__(self, color, trail, height, width, clone = False):
            super().__init__()

            self.clone = clone
            self.color = color
            self.trail = trail
            self.width = width
            self.height = height
            self.image = pygame.Surface([width, height])
            #self.image.fill(world_color)
            #self.image.set_colorkey(world_color)

            #pygame.draw.rect(pygame.Surface([width,height]),
            #                trail,
            #                pygame.Rect(0, 0, width, height))
            
            pygame.draw.rect(self.image,
                            color,
                            pygame.Rect(0, 0, width, height))

            self.rect = self.image.get_rect()    

        def getColors(self):
            return [self.color, self.trail]

        def getX(self):
            return self.rect.x
        
        def getY(self):
            return self.rect.y
        
        def moveRight(self, pixels):
            pygame.draw.rect(sample_surface, self.trail,
                            pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
            self.rect.x += pixels

        def moveLeft(self, pixels):
            pygame.draw.rect(sample_surface, self.trail,
                            pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
            self.rect.x -= pixels

        def moveUp(self, pixels):
            pygame.draw.rect(sample_surface, self.trail,
                            pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
            self.rect.y += pixels

        def moveDown(self, pixels):
            pygame.draw.rect(sample_surface, self.trail,
                            pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
            self.rect.y -= pixels

        def moveUpLeft(self, pixels):
            pygame.draw.rect(sample_surface, self.trail,
                            pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
            self.rect.x -= pixels
            self.rect.y += pixels

        def moveUpRight(self, pixels):
            pygame.draw.rect(sample_surface, self.trail,
                            pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
            self.rect.x += pixels
            self.rect.y += pixels

        def moveDownLeft(self, pixels):
            pygame.draw.rect(sample_surface, self.trail,
                            pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
            self.rect.y -= pixels
            self.rect.x -= pixels

        def moveDownRight(self, pixels):
            pygame.draw.rect(sample_surface, self.trail,
                            pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
            self.rect.y -= pixels
            self.rect.x += pixels
          
    
    def clone(cloned_sprite):
        new_sprite = Sprite(cloned_sprite.getColors()[0], cloned_sprite.getColors()[1], 20, 20)
        all_sprites_list.add(new_sprite)
        new_sprite.rect.x =  cloned_sprite.getX()
        new_sprite.rect.y = cloned_sprite.getY()
        return new_sprite
    
    def moveRandom(move_sprite):
        direction = random.choice(['left', 'right', 'up', 'down'])
        if direction == 'left' and move_sprite.rect.x > 2:
            move_sprite.moveLeft(22)
        if direction == 'right' and move_sprite.rect.x < display_size - 22:
            move_sprite.moveRight(22)
        if direction == 'down' and move_sprite.rect.y < display_size - 22:
            move_sprite.moveUp(22)
        if direction == 'up' and move_sprite.rect.y > 2:
            move_sprite.moveDown(22)

    def moveDirection(x, y, move_sprite):
        if x > 0:
            if y > 0 and move_sprite.rect.x < display_size - 22 and move_sprite.rect.y < display_size - 22:
                move_sprite.moveUpRight(22)
            if y == 0 and move_sprite.rect.x < display_size - 22:
                move_sprite.moveRight(22)
            if y < 0 and move_sprite.rect.x < display_size - 22 and move_sprite.rect.y > 2:
                move_sprite.moveDownRight(22)
        elif x == 0:
            if y > 0 and move_sprite.rect.y < display_size - 22:
                move_sprite.moveUp(22)
            if y < 0 and move_sprite.rect.y > 2:
                move_sprite.moveDown(22)
        elif x < 0:
            if y > 0 and move_sprite.rect.y < display_size - 22 and move_sprite.rect.x > 2:
                move_sprite.moveUpLeft(22)
            if y == 0 and move_sprite.rect.x > 2:
                move_sprite.moveLeft(22)
            if y < 0 and move_sprite.rect.x > 2 and move_sprite.rect.y > 2:
                move_sprite.moveDownLeft(22)

    def searchEmpty(moving_sprite):
        for x in range(1,num_cubes+1):
            search_list = []
            
            for i in range(-x, x+1):
                for j in range(-x, x+1):
                    search_list.append([i,j])
            print(search_list)
            while len(search_list) > 0:
                direction = random.choice(search_list)
                search_list.remove(direction)
                search_val = (moving_sprite.rect.x + direction[0] * 22, moving_sprite.rect.y + direction[1] * 22)
                #print(direction)
                if (search_val[0] >= 2 and search_val[0] <= display_size - 2) and (search_val[1] >= 2 and search_val[1] <= display_size - 2):
                    if sample_surface.get_at(search_val)[0:3] not in moving_sprite.getColors():
                        moveDirection(direction[0], direction[1], moving_sprite)
                        return
                
            
            print(search_list)

    def closeSearch(moving_sprite):
        curr_x = moving_sprite.rect.x
        curr_y = moving_sprite.rect.y

        close_list = [(-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0)]
        second_list = [(-2,2), (-2,1), (-2,0), (-2,-1), (-2,-2), 
                       (-1,2), (-1,1), (-1,0), (-1,-1), (-1,-2), 
                       (0,2), (0,1), (0,-1), (0,-2), 
                       (1,2), (1,1), (1,0), (1,-1), (1,-2), 
                       (2,2), (2,1), (2,0), (2,-1), (2,-2)]
        for non_used in range(len(close_list)):
            close_dict = {1:(-1,1), 2:(0,1), 3:(1,1), 4:(1,0), 5:(1,-1), 6:(0,-1), 7:(-1,-1), 8:(-1,0)}

            direction = random.choice(list(close_dict.items()))
            del close_dict[direction[0]]
            search_val = (curr_x + 22 * direction[1][0], curr_y + 22 * direction[1][1])
            #if search_val[0] > 2 and search_val[1] < 442:
            #    if sample_surface.get_at(search_val)[0:3] not in moving_sprite.getColors():
            #        
            #else:
            #    None        

    def moveTowardsEmpty(moving_sprite):
        curr_x = moving_sprite.rect.x
        curr_y = moving_sprite.rect.y
        for total_search in range(1,11):
            search_list = [] #use a search list instead of random choice
            for single_search in range(1,8):
                x_val = random.choice([0,-1, 1])
                y_val = random.choice([0,-1, 1])
                search_val = (total_search * x_val * 22 + curr_x, total_search * y_val * 22 + curr_y)
                print(search_val)
                if (search_val[0] > 0 and search_val[0] < 442) and (search_val[1] > 0 and search_val[1] < 442):
                    if sample_surface.get_at(search_val)[0:3] not in moving_sprite.getColors():
                        if x_val <= -1 and playerCar.rect.x > 2:
                            if y_val >= 1 and playerCar.rect.y < display_size - 22:
                                moving_sprite.moveUpLeft(22)
                                break
                            if y_val == 0:
                                moving_sprite.moveLeft(22)
                                break
                            if y_val <= -1 and playerCar.rect.y > 2:
                                moving_sprite.moveDownLeft(22)
                                break
                        if x_val >= 1 and playerCar.rect.x < display_size - 22:
                            if y_val >= 1 and playerCar.rect.y < display_size - 22:
                                moving_sprite.moveUpRight(22)
                                break
                            if y_val == 0:
                                moving_sprite.moveRight(22)
                                break
                            if y_val <= -1 and playerCar.rect.y > 2:
                                moving_sprite.moveDownRight(22)
                                break
                        if x_val == 0:
                            if y_val >= 1 and playerCar.rect.y < display_size - 22:
                                moving_sprite.moveUp(22)
                                break
                            if y_val == 0:
                                #moveRandom(moving_sprite)
                                break
                            if y_val <= -1 and playerCar.rect.y > 2:
                                moving_sprite.moveDown(22)
                                break
                        break
                    break
                
            break



    def checkMap():
        color_count = 0
        for x in range(5, 442, 22):
            for y in range(5, 442, 22):
                if sample_surface.get_at((x,y))[0:3] == (0,0,0):
                    color_count += 1
        return color_count

    pygame.init()
 
    
    RED = (255, 0, 0)
    ORANGE = (255, 100, 0)

    BLUE = (0, 0, 255)
    GREENISHBLUE = (0, 255, 255)
    
    size = (display_size, display_size)
    #screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Creating Sprite")
    
    all_sprites_list = pygame.sprite.Group()
    playerCar = Sprite(RED, ORANGE, 20, 20)
    playerCar.rect.x = 2
    playerCar.rect.y = 2
    
    all_sprites_list.add(playerCar)

    #playerCar2 = clone(playerCar)

    #print(playerCar2 in all_sprites_list)

    exit = True
    clock = pygame.time.Clock()

    while exit:
        #print('here')
        
        #print(color_count)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    exit = False

        #
        # moveRandom(playerCar)
        #moveTowardsEmpty(moving_sprite)
        #print(playerCar.rect.x)
        #print(playerCar.rect.y)
        
        #if (random.random()) > 0.95:
            #moveRandom(playerCar)
        #else:
        searchEmpty(playerCar)
        
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_LEFT] and playerCar.rect.x > 2:
        #     playerCar.moveLeft(22)
        # if keys[pygame.K_RIGHT] and playerCar.rect.x < display_size - 22:
        #     playerCar.moveRight(22)
        # if keys[pygame.K_DOWN] and playerCar.rect.y < display_size - 22:
        #     playerCar.moveUp(22)
        # if keys[pygame.K_UP]  and playerCar.rect.y > 2:
        #     playerCar.moveDown(22)
        
        # if playerCar2 in all_sprites_list:
        #     keys2 = pygame.key.get_pressed()
        #     if keys2[pygame.K_a] and playerCar2.rect.x > 2:
        #         playerCar2.moveLeft(22)
        #     if keys2[pygame.K_d] and playerCar2.rect.x < display_size - 22:
        #         playerCar2.moveRight(22)
        #     if keys2[pygame.K_s] and playerCar2.rect.y < display_size - 22:
        #         playerCar2.moveUp(22)
        #     if keys2[pygame.K_w]  and playerCar2.rect.y > 2:
        #         playerCar2.moveDown(22)
    
        all_sprites_list.update()
        #sample_surface.fill((200, 200, 200))

        #for i in range(0, display_size, range_gap):
        #    for j in range(0, display_size, range_gap):
        #        # Drawing Rectangle
        #        pygame.draw.rect(sample_surface, world_color,
        #                        pygame.Rect(i + line_width, j + line_width, cube_size, cube_size))
        all_sprites_list.draw(sample_surface)
        pygame.display.flip()
        clock.tick(10)
    
    pygame.quit()


#Main3()

