import pygame

# Initalize pygame
pygame.init()

# ---- create display window (surface) -----
# make constant height and width value for the window and initalize window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# set window title
pygame.display.set_caption('Hello World!')

# The main game loop
running = True
while running:
    # Loop through a list of Events object that have occured
    for event in pygame.event.get():
        print(event)

        # if user pressed the close button then close the loop
        if event.type == pygame.QUIT:
            running = False

# End the game - uninitalize any initalized pygame
pygame.quit()