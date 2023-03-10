# import pygame package
import pygame
import random

# initializing imported module
pygame.init()
  
def Main1():
    running = True

    cube_size = 20
    line_width = 2
    range_gap = cube_size + line_width
    color = (0,0,0)
    display_size = 442 # display_size = x(line_width) + y(cube_size), x = y+1 (one more line than cube)

    sample_surface = pygame.display.set_mode((display_size,display_size))
    
    sample_surface.fill((200, 200, 200))

    # Choosing red color for the rectangle


    for i in range(0, display_size, range_gap):
        for j in range(0, display_size, range_gap):
            # Drawing Rectangle
            pygame.draw.rect(sample_surface, color,
                            pygame.Rect(i + line_width, j + line_width, cube_size, cube_size))


    # Draws the surface object to the screen.
    pygame.display.update()

    # keep game running till running is true
    while running:
        
        # Check for event if user has pushed
        # any event in queue
        for event in pygame.event.get():
            
            # if event is of type quit then 
            # set running bool to false
            if event.type == pygame.QUIT:
                running = False
            # checking if keydown event happened or not
            if event.type == pygame.KEYDOWN:
                
                # checking if key "A" was pressed
                if event.key == pygame.K_a:
                    print("Key A has been pressed")
                
                # checking if key "J" was pressed
                if event.key == pygame.K_j:
                    print("Key J has been pressed")
                
                # checking if key "P" was pressed
                if event.key == pygame.K_p:
                    print("Key P has been pressed")
                
                # checking if key "M" was pressed
                if event.key == pygame.K_m:
                    print("Key M has been pressed")

def Main2():
    # GLOBAL VARIABLES
    COLOR = (255, 100, 98)
    SURFACE_COLOR = (167, 255, 100)
    WIDTH = 500
    HEIGHT = 500
    
    # Object class
    class Sprite(pygame.sprite.Sprite):
        def __init__(self, color, height, width):
            super().__init__()
    
            self.image = pygame.Surface([width, height])
            self.image.fill(SURFACE_COLOR)
            self.image.set_colorkey(COLOR)
    
            pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height))
    
            self.rect = self.image.get_rect()
    
    
    pygame.init()
  
    RED = (255, 0, 0)
    
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Creating Sprite")
    
    all_sprites_list = pygame.sprite.Group()
    
    object_ = Sprite(RED, 20, 30)
    object_.rect.x = 200
    object_.rect.y = 300
    
    all_sprites_list.add(object_)
    
    exit = True
    clock = pygame.time.Clock()
    
    while exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = False
    
        all_sprites_list.update()
        screen.fill(SURFACE_COLOR)
        all_sprites_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
 
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
        def __init__(self, color, height, width):
            super().__init__()

            self.image = pygame.Surface([width, height])
            self.image.fill(world_color)
            self.image.set_colorkey(world_color)

            pygame.draw.rect(self.image,
                            color,
                            pygame.Rect(0, 0, width, height))

            self.rect = self.image.get_rect()

        def moveRight(self, pixels):
            self.rect.x += pixels

        def moveLeft(self, pixels):
            self.rect.x -= pixels

        def moveForward(self, pixels):
            self.rect.y += pixels

        def moveBack(self, pixels):
            self.rect.y -= pixels
    pygame.init()
 
 
    RED = (255, 0, 0)
    
    
    size = (display_size, display_size)
    #screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Creating Sprite")
    
    
    all_sprites_list = pygame.sprite.Group()
    
    playerCar = Sprite(RED, 20, 20)
    playerCar.rect.x = 2
    playerCar.rect.y = 2
    
    
    all_sprites_list.add(playerCar)
    
    exit = True
    clock = pygame.time.Clock()
    
    while exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    exit = False
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerCar.moveLeft(22)
        if keys[pygame.K_RIGHT]:
            playerCar.moveRight(22)
        if keys[pygame.K_DOWN]:
            playerCar.moveForward(22)
        if keys[pygame.K_UP]:
            playerCar.moveBack(22)
    
        all_sprites_list.update()
        sample_surface.fill((200, 200, 200))

        for i in range(0, display_size, range_gap):
            for j in range(0, display_size, range_gap):
                # Drawing Rectangle
                pygame.draw.rect(sample_surface, world_color,
                                pygame.Rect(i + line_width, j + line_width, cube_size, cube_size))
        all_sprites_list.draw(sample_surface)
        pygame.display.flip()
        clock.tick(10)
    
    pygame.quit()



Main3()