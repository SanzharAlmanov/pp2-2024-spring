import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Clock")

width, height = 800, 800
R = min(width, height) // 3
ml = R * 3 // 4
sl = R - 10

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (255, 255, 255), (width // 2, height // 2), R, 4)

    for num in range(1, 13):
        angle = math.radians(90 - num * 30)  
        num_x = width // 2 + int(math.cos(angle) * R * 0.85)
        num_y = height // 2 - int(math.sin(angle) *R * 0.85)
        font = pygame.font.Font(None, 36)
        number_text = font.render(str(num), True, (255, 255, 255))
        num_rect = number_text.get_rect(center=(num_x, num_y))
        screen.blit(number_text, num_rect)

    current_time = pygame.time.get_ticks() // 1000
    minute = (current_time // 60) % 60
    second = current_time % 60

    minan = math.radians(360 - (minute + second / 60) * 6)  
    minx = width // 2 + int(math.cos(minan) * ml)
    miny = height // 2 - int(math.sin(minan) * ml)
    pygame.draw.line(screen, (255, 255, 255), (width // 2, height // 2), (minx, miny), 3)

    secan = math.radians(360 - second * 6)
    secx = width // 2 + int(math.cos(secan) * sl)
    secy = height // 2 - int(math.sin(secan) * sl)
    pygame.draw.line(screen, (255, 0, 0), (width // 2, height // 2), (secx, secy), 1)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
