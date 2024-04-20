import pygame
from datetime import datetime
import math

pygame.init()

# Set up screen
h = 800
w = 900
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Salomon')

# Load images
img_main = pygame.image.load("MICKEYC.png")
scaled_img = pygame.transform.scale(img_main, (w, h))
s = pygame.image.load("f.png").convert_alpha()
f = pygame.image.load("s.png").convert_alpha()
ns = pygame.transform.scale(s, (40, 300))
nf = pygame.transform.scale(f, (80, 200))

# Set initial positions
center_x = w // 2
center_y = h // 2

# Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Get current time
    current_time = datetime.now()
    seconds = current_time.second
    minutes = current_time.minute
    hours = current_time.hour % 12  # 12-hour format
    
    # Calculate angles for hands
    seconds_angle = math.radians(6 * seconds)  # 360 degrees / 60 seconds = 6 degrees per second
    minutes_angle = math.radians(6 * minutes + 0.1 * seconds)  # 360 degrees / 60 minutes = 6 degrees per minute
    hours_angle = math.radians(30 * hours + 0.5 * minutes)  # 360 degrees / 12 hours = 30 degrees per hour

    # Rotate images
    rotated_nf = pygame.transform.rotate(nf, math.degrees(seconds_angle))
    rotated_ns = pygame.transform.rotate(ns, math.degrees(hours_angle))

    # Calculate positions
    nf_x = center_x - rotated_nf.get_width() // 2
    nf_y = center_y - rotated_nf.get_height() + 20  # Adjusted to align with the center
    ns_x = center_x - rotated_ns.get_width() // 2
    ns_y = center_y - rotated_ns.get_height() + 50  # Adjusted to align with the center

    # Clear screen
    screen.fill((255, 255, 255))

    # Blit images
    screen.blit(scaled_img, (0, 0))
    screen.blit(rotated_nf, (nf_x, nf_y))
    screen.blit(rotated_ns, (ns_x, ns_y))

    pygame.display.update()

pygame.quit()
