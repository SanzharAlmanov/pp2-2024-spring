import pygame

pygame.init() #for initialization
screen = pygame.display.set_mode((600,700)) #display
pygame.display.set_caption("Salomon")
icon = pygame.image.load("MyIcon.png.webp")
pygame.display.set_icon(icon)
running = True
while running:
    screen.fill((61, 79, 107))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            
    
    

print("Finsihed")