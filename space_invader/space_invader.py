import pygame, random

# initalize pygame
pygame.init()

# set display surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Invaders')

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)

# Define a game class
class Game():
    # A class to help control and update gameplay
    def __init__(self):
        # Initalize the game
        pass

    def update(self):
        # Update the game
        pass

    def draw(self):
        # Draw hud and other information to display
        pass

    def shit_aliens(self):
        # Shift a wave of aleins down the screen and reverse direction
        pass

    def check_collision(self):
        # Check for collision
        pass

    def start_new_round(self):
        # start a new round
        pass

    def check_round_completion(self):
        # check to see if a player has completed a single round
        pass

    def check_game_status(self):
        # check to see the status of the game and how player died
        pass

    def pause_game(self):
        # Pasuses the game
        pass

    def reset_game(self):
        # resets the game
        pass

class Player(pygame.sprite.Sprite):
    # A class to model a spaceship the user can control

    def __init__(self, bullet_group):
        # initalize the player
        super().__init__()
        self.image = pygame.image.load('assets/images/player_ship.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH // 2
        self.rect.bottom = WINDOW_HEIGHT

        self.lives = 5
        self.velocity = 8

        self.bullet_group = bullet_group
        self.shoot_sound = pygame.mixer.Sound('assets/sounds/player_fire.wav')


    def update(self):
        # Update the player
        keys = pygame.key.get_pressed()

        # Move the player within bounds of the screen
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.velocity
        
        if keys[pygame.K_d] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity

    def fire(self):
        # fire a bullet
        # Restrict the number of bullets on screen at a time
        if len(self.bullet_group) < 2:
            self.shoot_sound.play()
            PlayerBullet(self.rect.centerx, self.rect.top, self.bullet_group)

    def reset(self):
        # reset player position
        self.rect.centerx = WINDOW_WIDTH // 2

class Alien(pygame.sprite.Sprite):
    # A class to model a alien spaceship the user can control

    def __init__(self, x, y, velocity, bullet_group):
        # initalize the alien
        super().__init__()
        self.image = pygame.image.load('assets/images/alien.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.initial_x = x
        self.initial_y = y

        self.direction = 1
        self.velocity = velocity
        self.bullet_group = bullet_group

        self.shoot_sound = pygame.mixer.Sound('assets/sounds/alien_fire.wav')

    def update(self):
        # Update the alien
        self.rect.x += self.direction * self.velocity

        # randomly fire a bullet
        if random.randint(0, 1000) > 999 and len(self.bullet_group) < 3:
            self.fire()

    def fire(self):
        # fire a bullet
        self.shoot_sound.play()
        AlienBullet(self.rect.centerx, self.rect.bottom, self.bullet_group)


    def reset(self):
        # reset alien position
        self.rect.topleft = (self.starting_x, self.starting_y)
        self.direction = 1


class PlayerBullet(pygame.sprite.Sprite):
    # A class to model a bullet fired by player
    def __init__(self, x, y, bullet_group):
        # Initialize the bullet
        super().__init__()
        self.image = pygame.image.load('assets/images/green_laser.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.velocity = 10
        bullet_group.add(self)

    def update(self):
        # update the bullet
        self.rect.y -= self.velocity

        # if the bullet is off the screen, remove it
        if self.rect.bottom < 0:
            self.kill()

class AlienBullet(pygame.sprite.Sprite):
    # A class to model a bullet fired by alein
    def __init__(self, x, y, bullet_group):
        # Initialize the bullet
        super().__init__()
        self.image = pygame.image.load('assets/images/red_laser.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.velocity = 10
        bullet_group.add(self)


    def update(self):
        # update the bullet
        self.rect.y += self.velocity

        # if the bullet is off the screen, destory it
        if self.rect.bottom > WINDOW_HEIGHT:
            self.kill()
        

# Create a bullet groups
my_player_bullet_group = pygame.sprite.Group()
my_alien_bullet_group = pygame.sprite.Group()

# Create a player group and Player object
my_player_group = pygame.sprite.Group()
my_player = Player(my_player_bullet_group)
my_player_group.add(my_player)

# Create an alien group. Will add Alien objects via the game's start a new round method
my_alien_group = pygame.sprite.Group()

# test alien
for  i in range(10):
    alien = Alien(64 + i * 64, 100, 1, my_alien_bullet_group)
    my_alien_group.add(alien)

# Create a game object
my_game = Game()

# The main game loop
running = True
while running:
    # Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # player wants to fire
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                my_player.fire()
    
    # Fill the display
    display_surface.fill(BLACK)

    # Update and display all sprite groups
    my_player_group.update()
    my_player_group.draw(display_surface)

    my_alien_group.update()
    my_alien_group.draw(display_surface)

    my_player_bullet_group.update()
    my_player_bullet_group.draw(display_surface)

    my_alien_bullet_group.update()
    my_alien_bullet_group.draw(display_surface)

    # Update and draw Game Object
    my_game.update()
    my_game.draw()

    # Update the display and tick clock
    pygame.display.update()
    clock.tick(FPS)

# End the game
pygame.quit()
