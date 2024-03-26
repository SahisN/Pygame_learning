import pygame
import random

# Initalize pygame
pygame.init()

# set display window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("~~Snake~~")

# Set FPS and clock
FPS = 20
clock = pygame.time.Clock()

# Set game values
SNAKE_SIZE = 20

head_x = WINDOW_WIDTH // 2
head_y = WINDOW_HEIGHT // 2 + 100

snake_dx = 0
snake_dy = 0

score = 0

# Set colors
GREEN = (0, 255, 0)
DARK_GREEN = (10, 50, 10)
RED = (255, 0, 0)
DARK_RED = (150, 0, 0)
WHITE = (255, 255, 255)

# Set fonts
font = pygame.font.SysFont('gabriola', 48)

# Set text
title_text = font.render('~~Snake~~', True, GREEN, DARK_RED)
title_rect = title_text.get_rect()
title_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

score_text = font.render(f'Score: {str(score)}', True, GREEN, DARK_RED)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

game_over_text = font.render('GAMEOVER', True, RED, DARK_GREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

continue_text = font.render('Press any key to play again', True, RED, DARK_GREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 64)

# Set sounds and music
pick_up_sound = pygame.mixer.Sound('sounds/pick_up_sound.wav')

# Set images - (top-left, x,  y, width, height)
apple_xy = (500, 500, SNAKE_SIZE,  SNAKE_SIZE)
apple_rect = pygame.draw.rect(window, GREEN, apple_xy)
head_xy = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw.rect(window, RED, head_xy)
body_xy = []

# The main game loop
running = True
while running:
    # Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Move the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -1 * SNAKE_SIZE
                snake_dy = 0
            
            if event.key == pygame.K_RIGHT:
                snake_dx = SNAKE_SIZE
                snake_dy = 0
            
            if event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -1 * SNAKE_SIZE
            
            if event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dy = SNAKE_SIZE

    # Add the head coordinate to the first index of the body coordinate list
    # This will essentially move all the snakes body by one position in the list
    body_xy.insert(0, head_xy)
    body_xy.pop()    

    # update the x, y position of the snake head and make new coordinate
    head_x += snake_dx
    head_y += snake_dy
    head_xy = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

    # Check for game over
    if head_rect.left < 0 or head_rect.right > WINDOW_WIDTH or head_rect.top < 0 or head_rect.bottom > WINDOW_HEIGHT or head_xy in body_xy:
        window.blit(game_over_text, game_over_rect)
        window.blit(continue_text, continue_rect)
        pygame.display.update()

        # Pause the game until the player presses a key, then reset the game
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                # The player wants to play again
                if event.type == pygame.KEYDOWN:
                    # reset score and position
                    score = 0
                    head_x = WINDOW_WIDTH // 2
                    head_y = WINDOW_HEIGHT // 2 + 100
                    head_xy = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

                    body_xy = []

                    snake_dx = 0
                    snake_dy = 0

                    is_paused = False

                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    # Check for collisions
    if head_rect.colliderect(apple_rect):
        score += 1
        pick_up_sound.play()

        apple_x = random.randint(0, WINDOW_WIDTH - SNAKE_SIZE)
        apple_y = random.randint(0, WINDOW_HEIGHT - SNAKE_SIZE)
        apple_xy = (apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE)

        body_xy.append(head_xy)

        # update score
        score_text = font.render(f'Score: {str(score)}', True, GREEN, DARK_RED)

    # fill the surface
    window.fill(WHITE)

    # blit hud
    window.blit(title_text, title_rect)
    window.blit(score_text, score_rect)

    # Blit assets
    for body in body_xy:
        pygame.draw.rect(window, DARK_GREEN, body)

    head_rect = pygame.draw.rect(window, GREEN, head_xy)
    apple_rect = pygame.draw.rect(window, RED, apple_xy)
    
    # update screen
    pygame.display.update()

    # tick the clock
    clock.tick(FPS)

# End the game
pygame.quit()