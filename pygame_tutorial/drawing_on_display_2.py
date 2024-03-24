import pygame

# Initailize Pygame
pygame.init()

# Create a display surface (screen) and set its caption (screen-title)
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")

# Define colors as RGB tuples
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# change background color
display_surface.fill(BLUE)

# Draw various shape on our display
# Line(surface, color, starting point, ending point, thickness) - requirements
pygame.draw.line(display_surface, RED, (0, 0), (100, 100), 5)
pygame.draw.line(display_surface, GREEN, (100, 100), (200, 300), 1)

# Circle (surface, color, center, radius, thickness)
pygame.draw.circle(display_surface, WHITE, (WINDOW_HEIGHT//2, WINDOW_WIDTH//2), 200, 6)
pygame.draw.circle(display_surface, YELLOW, (WINDOW_WIDTH // 2, WINDOW_HEIGHT / 2), 195, 0)

# Rectangle (surface, color, (top-left: x, top-left: y, width, height))
pygame.draw.rect(display_surface, CYAN, (500, 0, 100, 100))
pygame.draw.rect(display_surface, MAGENTA, (500, 100, 50, 100))

# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.update()

# End the game
pygame.quit()