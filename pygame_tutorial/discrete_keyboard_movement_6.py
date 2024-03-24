import pygame

# initalize pygame
pygame.init()

# Create our display
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Discrete Movement!")

# set game values
VELOCITY = 30

# Load in images
dragon_image = pygame.image.load('assets\images\dragon_right.png')
dragon_rect = dragon_image.get_rect()
dragon_rect.centerx = WINDOW_WIDTH // 2
dragon_rect.bottom = WINDOW_HEIGHT

# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for discrete movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dragon_rect.x -= VELOCITY
            
            if event.key == pygame.K_RIGHT:
                dragon_rect.x += VELOCITY
            
            if event.key == pygame.K_UP:
                dragon_rect.y -= VELOCITY
            
            if event.key == pygame.K_DOWN:
                dragon_rect.y += VELOCITY
    
    # Fill the display surface to cover old images
    screen.fill((0, 0, 0))

    # Blit (copy) assets to the screen
    screen.blit(dragon_image, dragon_rect)

    # update the game screen
    pygame.display.update()

# end the game 
pygame.quit()