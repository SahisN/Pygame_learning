import pygame
import random

# Initalize pygame
pygame.init()

# Set display window
WINDOW_WIDTH, WINDOW_HEIGHT = 945, 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Catch the Clown")

# set fps and clock
FPS = 60
clock = pygame.time.Clock()

# set game values
PLAYER_STARTING_LIVES = 5
CLOWN_STARTING_VELOCITY = 1
CLOWN_ACCELERATION = .5

score = 0
player_lives = PLAYER_STARTING_LIVES

clown_velocity = CLOWN_STARTING_VELOCITY
clown_dx = random.choice([-1, 1])
clown_dy = random.choice([-1, 1])

# set colors
BLUE = (1, 175, 209)
YELLOW = (248, 231, 28)

# set fonts
font = pygame.font.Font('assets/fonts/Franxurter.ttf', 32)

# set text
title_text = font.render('Catch the Clown', True, BLUE)
title_rect = title_text.get_rect()
title_rect.topleft = (50, 10)

score_text = font.render(f'Score: {str(score)}', True, YELLOW)
score_rect = score_text.get_rect()
score_rect.topright = (WINDOW_WIDTH - 50, 10)

lives_text = font.render(f'Lives: {str(player_lives)}', True, YELLOW)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 50, 50)

game_over_text = font.render('GAMEOVER', True, BLUE, YELLOW)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

continue_text = font.render('Click anywhere to play again', True, YELLOW, BLUE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 64)

# set sound and music
click_sound = pygame.mixer.Sound('assets/sounds/click_sound.wav')
miss_sound = pygame.mixer.Sound('assets/sounds/miss_sound.wav')
pygame.mixer.music.load('assets/sounds/ctc_background_music.wav')

# set images
background_image = pygame.image.load('assets/images/background.png')
background_rect = background_image.get_rect()
background_rect.topleft = (0, 0)

clown_image = pygame.image.load('assets/images/clown.png')
clown_rect = clown_image.get_rect()
clown_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)


# The main game loop
pygame.mixer.music.play(-1, 0, 0)
running = True
while running:
    # check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # check if a click is made
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            # Check if the clown was clicked
            if clown_rect.collidepoint(mouse_x, mouse_y):
                # increase the score & clown's velocity
                click_sound.play()
                score += 1
                clown_velocity += CLOWN_ACCELERATION

                # update the score
                score_text = font.render(f'Score: {str(score)}', True, YELLOW)

                # move the clown to new direction
                previous_dx, previous_dy = clown_dx, clown_dy
                while previous_dx == clown_dx and previous_dy == clown_dy:
                    clown_dx = random.choice([-1, 1])
                    clown_dy = random.choice([-1, 1])
            
            # when a clicked is miss
            else:
                # decrement lives
                miss_sound.play()
                player_lives -= 1

                # update player lives
                lives_text = font.render(f'Lives: {str(player_lives)}', True, YELLOW)
               
    
    # Move the clown
    clown_rect.x += clown_dx * clown_velocity
    clown_rect.y += clown_dy * clown_velocity

    # Bounce the clown of the edges of the screen
    if clown_rect.left <= 0 or clown_rect.right >= WINDOW_WIDTH:
        clown_dx *= -1
    
    if clown_rect.top <= 0 or clown_rect.bottom >= WINDOW_HEIGHT:
        clown_dy *= -1

    # check for game over
    if player_lives == 0:
        window.blit(game_over_text, game_over_rect)
        window.blit(continue_text, continue_rect)
        
        pygame.display.update()

        # pause the game until player clicks then reset the game
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES

                    clown_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
                    clown_velocity = CLOWN_STARTING_VELOCITY
                    clown_dx = random.choice([-1, 1])
                    clown_dy = random.choice([-1, 1])

                    pygame.mixer.music.play(-1, 0 , 0)
                    is_paused = False

                    # update the score and lives
                    score_text = font.render(f'Score: {str(score)}', True, YELLOW)
                    lives_text = font.render(f'Lives: {str(player_lives)}', True, YELLOW)
                
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    # blit the background
    window.blit(background_image, background_rect)
    
    # blit HUD
    window.blit(title_text, title_rect)
    window.blit(score_text, score_rect)
    window.blit(lives_text ,lives_rect)

    # Bilt assets
    window.blit(clown_image, clown_rect)

    # update the display
    pygame.display.update()

    # tick the clock
    clock.tick(FPS)    