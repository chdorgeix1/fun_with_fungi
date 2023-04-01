import pygame
import pygame_menu
pygame.init()

global map_size


# the following pygame menu allows a user to choose a species, map size, and whether a player
#  is a human or computer
# the user can also choose to play the game or exit the program

def start_the_game():
    # do the job here !
    pass

# Define callback function for selector
def set_map_size(selected_value, selector):
    global map_size
    print(f"Selected value: {selected_value[0][0]}")

global continue_menu

def end_menu():
    global continue_menu
    continue_menu = False

def on_button1_click():
    print("Button 1 clicked")

def on_button2_click():
    print("Button 2 clicked")

def on_button3_click():
    print("Button 3 clicked")

def run_menu():
    continue_menu = True
    # set the screen size
    screen = pygame.display.set_mode((640, 480))

    # set the title of the window
    pygame.display.set_caption("Evolution")

    # create the menu
    menu = pygame_menu.Menu('Welcome', 640, 480, 
                            theme=pygame_menu.themes.THEME_DARK)

    # create the menu options
    choices = [('Small', 1), ('Medium', 2), ('Large', 3)]
    map_size_selector = menu.add.selector('S1:', choices, onchange=set_map_size)
    map_size_selector.set_background_color((200, 200, 200))

    player_1_select = menu.add.selector('Sp:', choices, onchange=set_map_size)
    player_1_select.set_background_color((0, 200, 200))
    
    player_2_select = menu.add.selector('Select Player 2 Species:', choices, onchange=set_map_size)
    player_2_select.set_background_color((200, 0, 200))

    player_2_human = menu.add.selector('Select Player 2 Person/Computer:', choices, onchange=set_map_size)
    player_2_human.set_background_color((200, 200, 0))
    
    play_button = menu.add.button('Play', end_menu)


    play_button.set_background_color((0, 200, 0))
    quit_button = menu.add.button('Quit', pygame_menu.events.EXIT)
    quit_button.set_background_color((200, 0, 0))
    # start the menu
    if continue_menu:
        menu.mainloop(screen)

        
    # surface = pygame.display.set_mode((500,500))
    # menu = pygame_menu.Menu('Welcome', 500, 500, theme = pygame_menu.themes.THEME_BLUE)

    # menu.add.button("Set Player 1 Species: 0", changeP1Species0)
    # menu.add.button("Set Player 1 Species: 1", changeP1Species1)
    # menu.add.button("Set Player 1 Species: 2", changeP1Species2)
    # menu.add.button("Set Player 2 Species: 0", changeP2Species0)
    # menu.add.button("Set Player 2 Species: 1", changeP2Species1)
    # menu.add.button("Set Player 2 Species: 2", changeP2Species2)


    # #species_button = menu.add.selector('Difficulty:', [('durablefungi', 0), ('whateverfungi', 1)], onchange=set_player_species)
    # menu.add.button("Start Game", testMain)
    # #menu.add.button('Play', testMain(True))
    # menu.mainloop(surface)




run_menu()