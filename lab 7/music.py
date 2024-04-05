import pygame
import os

pygame.init()

screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Sanzhar's music")

WHITE = (255, 255, 255)

music_dir = "C:\\Users\\user\\Music"

songs = os.listdir(music_dir)
curindex = 0

pygame.mixer.music.load(os.path.join(music_dir, songs[curindex]))

running = True
paused = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
            elif event.key == pygame.K_n:
                curindex = (curindex + 1) % len(songs)
                pygame.mixer.music.load(os.path.join(music_dir, songs[curindex]))
                pygame.mixer.music.play()
            elif event.key == pygame.K_p:
                curindex = (curindex - 1) % len(songs)
                pygame.mixer.music.load(os.path.join(music_dir, songs[curindex]))
                pygame.mixer.music.play()

    screen.fill(WHITE)

    pygame.display.flip()

pygame.quit()