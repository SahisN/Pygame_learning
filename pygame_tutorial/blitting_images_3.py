import pygame

# Initailize pygame
pygame.init()

# Creating a display
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Blitting Images!')

# Create images... returns a surface object with the image drawn on it
# We can get the rect of the surface and use the rect to position the image
dragon_left_image = pygame.image.load('pygame_tutorial/assets/images/dragon_left.png')
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0, 0)

dragon_right_image = pygame.image.load('pygame_tutorial/assets/images/dragon_right.png')
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (WINDOW_WIDTH, 0)

# bliting images - copying premade image into the game


# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # bliting images - copying premade image into the game
    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)

    pygame.draw.line(display_surface, (255, 255, 255), (0, 75), (WINDOW_WIDTH, 75), 4)

    # update the display
    pygame.display.update()

# End the game
pygame.quit() 