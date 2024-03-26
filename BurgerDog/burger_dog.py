import pygame
import random

# initalize pygame
pygame.init()

# set game display & caption
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Burger Dog')

# set fps and clock
FPS = 60
clock = pygame.time.Clock()

# set game values
PLAYER_STARTING_LIVES = 3
PLAYER_NORMAL_VELOCITY = 5
PLAYER_BOOST_VELOCITY = 10
STARTING_BOOST_LEVEL = 100
STARTING_BURGER_VELOCITY = 3
BURGER_ACCELRATION = .5
BUFFER_DISTANCE = 100

score = 0
burger_points = 0
burger_eaten = 0

player_lives = PLAYER_STARTING_LIVES
player_velocity = PLAYER_NORMAL_VELOCITY
boost_level = STARTING_BOOST_LEVEL
burger_velocity = STARTING_BURGER_VELOCITY

# set colors
ORANGE = (246, 170, 54)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# set fonts
font = pygame.font.Font('assets/fonts/WashYourHand.ttf', 32)

# set texts
points_text = font.render(f'Burger Points: {str(burger_points)}', True, ORANGE)
points_rect = points_text.get_rect()
points_rect.topleft = (10, 10)

score_text = font.render(f'Score: {str(score)}', True, ORANGE)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 50)

title_text = font.render('Burger Dog', True, ORANGE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH // 2
title_rect.y = 10

eaten_text = font.render(f'Burgers Eaten: {str(burger_eaten)}', True, ORANGE)
eaten_rect = eaten_text.get_rect()
eaten_rect.centerx = WINDOW_WIDTH // 2
eaten_rect.y = 50

lives_text = font.render(f'Lives: {str(player_lives)}', True, ORANGE)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)

boost_text = font.render(f'Boost: {str(boost_level)}', True, ORANGE)
boost_rect = boost_text.get_rect()
boost_rect.topright = (WINDOW_WIDTH - 10, 50)

game_over_text = font.render(f'FINAL SCORE: {str(score)}', True, ORANGE)
game_over_rect =  game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

continue_text = font.render('Press any key to play again', True, ORANGE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 64)

# set sound and music
bark_sound = pygame.mixer.Sound('assets/sounds/bark_sound.wav')
miss_sound = pygame.mixer.Sound('assets/sounds/miss_sound.wav')
pygame.mixer.music.load('assets/sounds/bd_background_music.wav')

# set images
player_image_right = pygame.image.load('assets/images/dog_right.png')
player_image_left = pygame.image.load('assets/images/dog_left.png')
player_image = player_image_left
player_rect = player_image.get_rect()
player_rect.centerx = WINDOW_WIDTH // 2
player_rect.bottom = WINDOW_HEIGHT

burger_image = pygame.image.load('assets/images/burger.png')
burger_rect = burger_image.get_rect()
burger_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), - BUFFER_DISTANCE)

# The main game loop
pygame.mixer.music.play(-1, 0, 0)
running = True
while running:
    # Check if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the surface
    window.fill(BLACK)

    # Move the player
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and player_rect.left > 0:
        player_rect.x -= player_velocity
        player_image = player_image_left
    
    if keys[pygame.K_d] and player_rect.right < WINDOW_WIDTH:
        player_rect.x += player_velocity
        player_image = player_image_right

    if keys[pygame.K_w] and player_rect.top > 100:
        player_rect.y -= player_velocity
    
    if keys[pygame.K_s] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += player_velocity
    
    # Engage the boost when player holds space
    if keys[pygame.K_SPACE] and boost_level > 0:
        player_velocity = PLAYER_BOOST_VELOCITY
        boost_level -= 1

    else:
        player_velocity = PLAYER_NORMAL_VELOCITY

    # Move the burger and update burger points
    burger_rect.y += burger_velocity
    burger_points = int(burger_velocity) *(WINDOW_HEIGHT - burger_rect.y + 100)

    # player missed the burger 
    if burger_rect.y > WINDOW_HEIGHT:
        player_lives -= 1
        miss_sound.play()

        burger_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), - BUFFER_DISTANCE)
        burger_velocity = STARTING_BURGER_VELOCITY

        player_rect.centerx = WINDOW_WIDTH // 2
        player_rect.bottom = WINDOW_HEIGHT

        boost_level = STARTING_BOOST_LEVEL

        

    
    
    # Check for collision
    if player_rect.colliderect(burger_rect):
        score += burger_points
        burger_eaten += 1
        bark_sound.play()

        burger_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), - BUFFER_DISTANCE)
        burger_velocity = STARTING_BURGER_VELOCITY

        boost_level += 25
        boost_level = STARTING_BOOST_LEVEL if boost_level > STARTING_BOOST_LEVEL else boost_level



    # check for game over
    if player_lives == 0:
        pygame.mixer_music.stop()
        lives_text = font.render('Lives: 0', True, ORANGE)
        game_over_text = font.render(f'FINAL SCORE: {str(score)}', True, ORANGE)
        window.blit(game_over_text, game_over_rect)
        window.blit(continue_text, continue_rect)
        pygame.display.update()

        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    score = 0 
                    burger_eaten = 0
                    player_lives = PLAYER_STARTING_LIVES
                    boost_level = STARTING_BOOST_LEVEL
                    burger_velocity = STARTING_BURGER_VELOCITY

                    pygame.mixer_music.play()
                    is_paused = False
                    

    # update hud
    lives_text = font.render(f'Lives: {str(player_lives)}', True, ORANGE)
    eaten_text = font.render(f'Burgers Eaten: {str(burger_eaten)}', True, ORANGE)
    score_text = font.render(f'Score: {str(score)}', True, ORANGE)
    boost_text = font.render(f'Boost: {str(boost_level)}', True, ORANGE)    
    points_text = font.render(f'Burger Points: {str(burger_points)}', True, ORANGE)                

    # Blit the hud
    window.blit(points_text, points_rect)
    window.blit(score_text, score_rect)
    window.blit(title_text, title_rect)
    window.blit(eaten_text, eaten_rect)
    window.blit(lives_text, lives_rect)
    window.blit(boost_text, boost_rect)
    pygame.draw.line(window, WHITE, (0, 100), (WINDOW_WIDTH, 100), 3)

    # Blit assets
    window.blit(player_image, player_rect)
    window.blit(burger_image, burger_rect)

    # Update the display
    pygame.display.update()

    # tick the clock
    clock.tick(FPS)

    
