import pygame 
import random
pygame.init()
w = 900
h = 600
score = 0
color = (68,76,56)
pygame.display.set_caption("CARS")
screen = pygame.display.set_mode((w,h))
car = pygame.image.load("car.png")
carimg = pygame.transform.scale(car,(150,150))
font = pygame.font.Font(None, 30)

run = 1
x = 380
y = 450
ml = False
mr = False
recta = carimg.get_rect()


enemy = pygame.image.load("enemy.png")
enemyimg = pygame.transform.scale(enemy,(150,150))
ex = random.randint(10,850)
ey = -100
espeed = 2
rectb = enemyimg.get_rect()

stime = pygame.time.get_ticks()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                ml = True
            elif event.key == pygame.K_d:
                mr = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                ml = False
            elif event.key == pygame.K_d:
                mr = False
    if ml:
        if x > 0:
            x -= 1
    if mr:
        if x < w - 150:
            x += 1

    ctime = pygame.time.get_ticks()        
    if stime - ctime >= 1000:
        espeed += 100
        stime = ctime

    if random.randint(1,200) < 100:
        ey += espeed
        if ey + 100 == 600:
            ey = -100
            ex = random.randint(50,850)
            score += 1

    recta.x = x
    recta.y = y
    rectb.x = ex
    rectb.y = ey
    
    text = font.render(f"Score: {score}", True, (255,255,255))

    if recta.colliderect(rectb):
        print(f"GAME OVER, your score is {score}" )
        run = False
    screen.fill(color)      
    screen.blit(carimg,(x,y))
    screen.blit(enemyimg,(ex,ey))
    screen.blit(text,(425,100))
    pygame.draw.line(screen,(255,255,255),(300,0),(300,600),5)       
    pygame.draw.line(screen,(255,255,255),(600,0),(600,600),5) 
    pygame.display.update()
    