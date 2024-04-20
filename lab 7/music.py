import pygame
import os

pygame.mixer.init()
pygame.init()

screen = pygame.display.set_mode((480, 248))
pygame.display.set_caption("Music Player")

music_dir = "C:\\Users\\user\\Desktop\\JOJO1\\lab 7"

if not os.path.exists(music_dir):
    print("Error: Music directory does not exist.")
    pygame.quit()
    quit()

songs = [os.path.join(music_dir, file) for file in os.listdir(music_dir) if file.endswith(".mp3")]

if not songs:
    print("Error: No MP3 files found in the music directory.")
    pygame.quit()
    quit()

current_music = 0
pos = 0
paused = False
pygame.mixer.music.load(songs[current_music])
pygame.mixer.music.play()

background = pygame.image.load("C:\\Users\\user\\Downloads\\player.png")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    pos = pygame.mixer.music.get_pos()
                    paused = True
            elif event.key == pygame.K_RIGHT:
                current_music = (current_music + 1) % len(songs)
                pygame.mixer.music.load(songs[current_music])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_music = (current_music - 1) % len(songs)
                pygame.mixer.music.load(songs[current_music])
                pygame.mixer.music.play()

    screen.blit(background, (0, 0))
    pygame.display.flip()

pygame.quit()
