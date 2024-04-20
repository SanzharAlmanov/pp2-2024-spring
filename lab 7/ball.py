import pygame 
import math

pygame.init()
w,h = 900,650
pygame.display.set_caption("Salomon")
screen = pygame.display.set_mode((w,h))
cx = w // 2
cy = h // 2
run = 1
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
            print("Finished")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if cx + 25 < w:
                    cx += 25
            elif event.key == pygame.K_a:
                if cx - 25 > 0:
                    cx -= 25
            elif event.key == pygame.K_w:
                if cy - 25 > 0:
                    cy -= 25
            elif event.key == pygame.K_s:
                if cy + 25 < h:
                    cy +=25  
    pygame.draw.circle(screen,(236,43,43),(cx, cy), 25,25)
    
    pygame.display.update()
    screen.fill((255,255,255))
pygame.quit()