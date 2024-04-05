import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

R = 25 
bx = WIDTH // 2 
by = HEIGHT // 2  
v = 20  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                by -= v
            elif event.key == pygame.K_DOWN:
                by += v
            elif event.key == pygame.K_LEFT:
                bx -= v
            elif event.key == pygame.K_RIGHT:
                bx += v
    if bx - R < 0:
        bx = R
    elif bx + R > WIDTH:
        bx = WIDTH - R
    if by - R < 0:
        by = R
    elif by + R > HEIGHT:
        by = HEIGHT - R

    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (bx, by), R)

    pygame.display.flip()

pygame.quit()
sys.exit()
