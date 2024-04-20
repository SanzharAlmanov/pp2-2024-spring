import pygame
import random

w = 800
h = 800
size = 50
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Snake")
hoto = pygame.image.load("zmeika.jpg")
photo = pygame.transform.scale(hoto, (800,800))
x = random.randrange(0, w, size)
y = random.randrange(0, h, size)

score = 0
superalma = (random.randrange(0, w, size), random.randrange(0, h, size))
alma = (random.randrange(0, w, size), random.randrange(0, h, size))
razmer = 1
zhylan = [(x, y)]
dx = 0
dy = 0
fps = 5
time = pygame.time.get_ticks()

clock = pygame.time.Clock()
run = 1
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_w and dy != 1:  
                dx, dy = 0, -1
            elif event.key == pygame.K_s and dy != -1:  
                dx, dy = 0, 1
            elif event.key == pygame.K_d and dx != -1:  
                dx, dy = 1, 0
            elif event.key == pygame.K_a and dx != 1:  
                dx, dy = -1, 0
    screen.fill((0, 0, 0))
    screen.blit(photo,(0,0))
    [(pygame.draw.rect(screen, (11, 102, 35), (i, j, size, size))) for i, j in zhylan]
    pygame.draw.rect(screen, (124, 10, 2), (*alma, size, size))
    pygame.draw.rect(screen, (0,0,255), (*superalma,size,size))
    x += dx * size
    y += dy * size
    zhylan.append((x, y))
    zhylan = zhylan[-razmer:]

    if zhylan[-1] == alma:
        alma = (random.randrange(0, w, size), random.randrange(0, h, size))
        razmer += 1
        score += 1
        fps += 1
        
    if zhylan[-1] == superalma:
        razmer += 3
        score += 3
        fps += 3
        superalma = (random.randrange(0, w, size), random.randrange(0, h, size))
        time = pygame.time.get_ticks()

    currentime = pygame.time.get_ticks()
    if currentime - time >= 3000:
        superalma = (random.randrange(0, w, size), random.randrange(0, h, size))
        time = currentime
    
    if x < 0 or x > w - size or y < 0 or y > h - size:
        run = 0
        print(f"Your score is {score}")
    if len(zhylan) != len(set(zhylan)):
        run = 0
        print(f"Your score is {score}")
    pygame.display.flip()
    clock.tick(fps)
