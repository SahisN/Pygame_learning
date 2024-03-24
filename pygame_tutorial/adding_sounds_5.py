import pygame

# initalize pygame
pygame.init()

# Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Adding sounds')

# load sound effects
sound_1 = pygame.mixer.Sound('assets\images\sound_1.wav')
sound_2 = pygame.mixer.Sound('assets\images\sound_2.wav')

# play the sound effects
sound_1.play()
pygame.time.delay(2000)
# sound_2.play()


# change the volume of a sound effect
sound_2.set_volume(.1)
sound_2.play()
pygame.time.delay(2000)

# load background music
pygame.mixer.music.load('assets\images\music.wav')

# play and stop the music
pygame.mixer.music.play(-1, 0, 0)
pygame.time.delay(1000)
sound_2.play()
pygame.time.delay(5000)
pygame.mixer.music.stop()

# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # update the game
    pygame.display.update()

# end game
pygame.quit()