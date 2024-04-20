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


coin1 = pygame.image.load("coin1.png")
coin2 = pygame.image.load("coin2.png")

coin1 = pygame.transform.scale(coin1, (100,100))
coin2 = pygame.transform.scale(coin2, (130,130))

rcoin1 = coin1.get_rect()
rcoin2 = coin2.get_rect()


coin1_x = 0
coin1_y = 0
coin2_x = 0
coin2_y = 0

enemy = pygame.image.load("enemy.png")
enemyimg = pygame.transform.scale(enemy,(150,150))
ex = random.randint(10,850)
ey = -100
espeed = 2
rectb = enemyimg.get_rect()
recta = carimg.get_rect()

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
        ey += espeed + (score*0.2)
        if ey + 100 >= 600:
            ey = -100
            ex = random.randint(50,850)
    if random.randint(1,200) < 150:
        coin1_y += 1
        if coin1_y > h:
            coin1_y = -100
            coin1_x = random.randint(50, 850)
        rcoin1.x = coin1_x
        rcoin1.y = coin1_y

    if random.randint(1,1000) < 900:
        coin2_y += 0.2
        if coin2_y > h:
            coin2_y = -100
            coin2_x = random.randint(50, 850)
        rcoin2.x = coin2_x
        rcoin2.y = coin2_y

    recta.x = x
    recta.y = y
    rectb.x = ex
    rectb.y = ey
    
    text = font.render(f"Score: {score}", True, (255,255,255))

    if recta.colliderect(rectb):
        print(f"GAME OVER, your score is {score}" )
        run = False
    if rcoin1.colliderect(recta):
            score += 1
            coin1_x = random.randint(50,850)
            if random.randint(1,200) < 150:
                coin1_y = -20
            else:
                coin1_y = -500

    if rcoin2.colliderect(recta):
            score += 5
            coin2_x = random.randint(50,850)
            coin2_y = -1000
           

    screen.fill(color)      
    screen.blit(carimg,(x,y))
    screen.blit(enemyimg,(ex,ey))
    screen.blit(text,(425,100))
    screen.blit(coin1, (coin1_x,coin1_y))
    screen.blit(coin2, (coin2_x, coin2_y))
    pygame.draw.line(screen,(255,255,255),(300,0),(300,600),5)       
    pygame.draw.line(screen,(255,255,255),(600,0),(600,600),5) 
    pygame.display.update()
    