import pygame
from datetime import datetime

pygame.init()

# Set up screen
h = 800
w = 900
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Salomon')

img_main = pygame.image.load("MICKEYC.png")
scaled_img = pygame.transform.scale(img_main, (w, h))
s = pygame.image.load("f.png")
f = pygame.image.load("s.png")
clock_rect = img_main.get_rect(center=(w // 2, h // 2))
sp = pygame.transform.scale(s,(50,200))
fp = pygame.transform.scale(f,(80,400))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    curtime = datetime.now().time()
    sec_angle = -curtime.second * 6  
    min_angle = -(curtime.minute * 6 + curtime.second / 10)  
    
    sec_rot = pygame.transform.rotate(fp, sec_angle)
    min_rot = pygame.transform.rotate(sp, min_angle)

    sec_rect = sec_rot.get_rect(center=clock_rect.center)
    min_rect = min_rot.get_rect(center=clock_rect.center)
    
    screen.fill((255, 255, 255))
    
    screen.blit(scaled_img, (0, 0))
    screen.blit(sec_rot, sec_rect)
    screen.blit(min_rot, min_rect)
    
    pygame.display.update()

pygame.quit()
