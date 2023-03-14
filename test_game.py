# import pygame package
import pygame
import random

# initializing imported module
pygame.init()
 
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
    display_size = 442 # display_size = x(line_width) + y(cube_size), x = y+1 (one more line than cube)

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

        def moveForward(self, pixels):
            pygame.draw.rect(sample_surface, self.trail,
                            pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
            self.rect.y += pixels

        def moveBack(self, pixels):
            pygame.draw.rect(sample_surface, self.trail,
                            pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
            self.rect.y -= pixels
          
    
    def clone(cloned_sprite):
        new_sprite = Sprite(cloned_sprite.getColors()[0], cloned_sprite.getColors()[1], 20, 20)
        all_sprites_list.add(new_sprite)
        new_sprite.rect.x =  cloned_sprite.getX()
        new_sprite.rect.y = cloned_sprite.getY()
        return new_sprite
    
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

    playerCar2 = clone(playerCar)

    print(playerCar2 in all_sprites_list)

    exit = True
    clock = pygame.time.Clock()

    while exit:
        #print('here')
        color_count = 0
        for x in range(5, 442, 22):
            for y in range(5, 442, 22):
                if sample_surface.get_at((x,y))[0:3] == (0,0,0):
                    color_count += 1
        #print(color_count)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    exit = False
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and playerCar.rect.x > 2:
            playerCar.moveLeft(22)
        if keys[pygame.K_RIGHT] and playerCar.rect.x < 420:
            playerCar.moveRight(22)
        if keys[pygame.K_DOWN] and playerCar.rect.y < 420:
            playerCar.moveForward(22)
        if keys[pygame.K_UP]  and playerCar.rect.y > 2:
            playerCar.moveBack(22)
        
        if playerCar2 in all_sprites_list:
            keys2 = pygame.key.get_pressed()
            if keys2[pygame.K_a] and playerCar2.rect.x > 2:
                playerCar2.moveLeft(22)
            if keys2[pygame.K_d] and playerCar2.rect.x < 420:
                playerCar2.moveRight(22)
            if keys2[pygame.K_s] and playerCar2.rect.y < 420:
                playerCar2.moveForward(22)
            if keys2[pygame.K_w]  and playerCar2.rect.y > 2:
                playerCar2.moveBack(22)
    
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



Main3()