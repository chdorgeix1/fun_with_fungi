# import pygame package
import pygame
  
# initializing imported module
pygame.init()
  

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


# GLOBAL VARIABLES
SPRITE_COLOR = (255, 100, 98)
SPRITE_SURFACE_COLOR = (167, 255, 100)
WIDTH = 500
HEIGHT = 500
  
# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
  
        self.image = pygame.Surface([width, height])
        self.image.fill(SPRITE_SURFACE_COLOR)
        self.image.set_colorkey(SPRITE_COLOR)
  
        pygame.draw.rect(self.image,
                         color,
                         pygame.Rect(0, 0, width, height))
  
        self.rect = self.image.get_rect()
 
