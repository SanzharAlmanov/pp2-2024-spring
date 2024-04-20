import pygame
import random

pygame.init()
SIZE = 20
w = 800
h = 800
blocks = 20
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("Snake")

run = 1
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0

    screen.fill((0,255,204))
    for column in range(blocks):
        if column % 2 == 0:
            color = ((204,255,255))
        else:
            color = ((255,255,255))
        pygame.draw.rect(screen,(color), [10 + column*blocks,20,SIZE,SIZE])
    pygame.display.flip()