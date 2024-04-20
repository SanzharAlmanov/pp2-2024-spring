import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mini Paint")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set default color
current_color = BLACK

# Set default brush size
brush_size = 5

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                current_color = RED
            elif event.key == pygame.K_g:
                current_color = GREEN
            elif event.key == pygame.K_b:
                current_color = BLUE
            elif event.key == pygame.K_c:
                screen.fill(WHITE)

    # Draw shapes
    if pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()
        if pygame.key.get_pressed()[pygame.K_s]:  # Draw square
            pygame.draw.rect(screen, current_color, (mouse_pos[0] - brush_size // 2, mouse_pos[1] - brush_size // 2, brush_size, brush_size))
        elif pygame.key.get_pressed()[pygame.K_t]:  # Draw right triangle
            pygame.draw.polygon(screen, current_color, [(mouse_pos[0], mouse_pos[1] - brush_size),
                                                         (mouse_pos[0] - brush_size, mouse_pos[1]),
                                                         (mouse_pos[0], mouse_pos[1])])
        elif pygame.key.get_pressed()[pygame.K_e]:  # Draw equilateral triangle
            side_length = brush_size * math.sqrt(3)
            pygame.draw.polygon(screen, current_color, [(mouse_pos[0], mouse_pos[1] - side_length),
                                                         (mouse_pos[0] - brush_size, mouse_pos[1] + brush_size),
                                                         (mouse_pos[0] + brush_size, mouse_pos[1] + brush_size)])
        elif pygame.key.get_pressed()[pygame.K_r]:  # Draw rhombus
            pygame.draw.polygon(screen, current_color, [(mouse_pos[0], mouse_pos[1] - brush_size),
                                                         (mouse_pos[0] - brush_size, mouse_pos[1]),
                                                         (mouse_pos[0], mouse_pos[1] + brush_size),
                                                         (mouse_pos[0] + brush_size, mouse_pos[1])])
        else:  # Draw circle (default)
            pygame.draw.circle(screen, current_color, mouse_pos, brush_size)

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
