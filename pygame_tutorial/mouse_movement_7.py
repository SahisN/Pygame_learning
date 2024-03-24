import pygame

# initalize pygame
pygame.init()

# Create a display surface
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 300
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Mouse Movement!")

# Load in images
dragon_image = pygame.image.load('assets\images\dragon_right.png')
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25, 25)


# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # listen to move event
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_rect.centerx = mouse_x
            dragon_rect.centery = mouse_y
        
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_rect.centerx = mouse_x
            dragon_rect.centery = mouse_y
        

        
    # Fill the display
    screen.fill((0,0,0))

    # Bilt assets
    screen.blit(dragon_image, dragon_rect)
            
    # update the screen
    pygame.display.update()
    
# End the game
pygame.QUIT