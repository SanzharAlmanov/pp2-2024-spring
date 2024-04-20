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
paused = False  # Variable to track whether the music is paused
paused_position = 0  # Variable to store the position where the music was paused

pygame.mixer.music.load(songs[current_music])
pygame.mixer.music.play()

while True:  # Main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    # Resume playback from the stored position
                    pygame.mixer.music.play(start=paused_position)
                    paused = False
                elif pygame.mixer.music.get_busy():
                    # Stop the music and store the current playback position
                    pygame.mixer.music.stop()
                    paused_position = pygame.mixer.music.get_pos()
                    paused = True
                else:
                    # If the music is not playing, start playing from the beginning
                    pygame.mixer.music.play()

    pygame.display.update()
