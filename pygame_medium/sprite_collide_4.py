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
class Player(pygame.sprite.Sprite):
    def __init__(self, x , y, monster_group):
        super().__init__()
        self.image = pygame.image.load('knight.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = 5
        self.monster_group = monster_group
    
    def move(self):
        # Move the player continously
        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_a]:
            self.rect.x -= self.velocity
        
        if key_pressed[pygame.K_d]:
            self.rect.x += self.velocity

        if key_pressed[pygame.K_w]:
            self.rect.y -= self.velocity
        
        if key_pressed[pygame.K_s]:
            self.rect.y += self.velocity

    def check_collision(self):
        # Check for collisions between player (self) and the monster group
        if pygame.sprite.spritecollide(self, self.monster_group, True):
            print(len(monster_group))
            

    def update(self):
        # update the player
        self.move()
        self.check_collision()
    

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

# Create a player group and add a player
player_group = pygame.sprite.Group()
player = Player(500, 500, monster_group)
player_group.add(player)    

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

    player_group.update()
    player_group.draw(display_surface)

    # update the screen
    pygame.display.update()

    # tick the clock
    clock.tick(FPS)



# end the game
pygame.quit()