import pygame
import random

# Initalize pygame
pygame.init()

# Set display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Sprite Groups!')

# set fps and clock
FPS = 60
clock = pygame.time.Clock()

# Define classes
class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('blue_monster.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = random.randint(1, 5)
    
    def update(self):
        # update and move the monster
        self.rect.y += self.velocity

# Create a monster group and add 10 monsters
monster_group = pygame.sprite.Group()
for i in range(10):
    monster = Monster(i * 64, 10)
    monster_group.add(monster)
        


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the display
    display_surface.fill((0,0,0))

    # Update assets and Draw
    monster_group.update()
    monster_group.draw(display_surface)

    # update the screen
    pygame.display.update()

    # tick the clock
    clock.tick(FPS)



# end the game
pygame.quit()