import pygame
from datetime import datetime
import math

pygame.init()
minute = second = 0

h = 650
w = 900
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Salomon')
img_main = pygame.image.load("MICKEYC.png")
run = True
scaled_img = pygame.transform.scale(img_main, (w, h))

def draw_hand(color, angle, length, thickness):
    angle -= 90
    angle_rad = math.radians(angle)
    x = w // 2 + length * math.cos(angle_rad)
    y = h // 2 + length * math.sin(angle_rad)
    pygame.draw.line(screen, color, (w // 2, h // 2), (x, y), thickness)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    timee = datetime.now().time()  

    m_angle = (timee.minute / 60) * 360
    s_angle = (timee.second / 60) * 360
    h_angle = (timee.hour % 12) / 12 * 360 + (timee.minute / 60) * 30
 
    screen.blit(scaled_img,(0,0))

    draw_hand((0,0,0), h_angle, min(w,h)//4, 7)
    draw_hand((0,0,0), m_angle, min(h,w)//3, 4)
    draw_hand((0,0,0), s_angle, min(h,w)//2, 2)

    
    pygame.display.update()