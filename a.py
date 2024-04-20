import pygame
import os

pygame.mixer.init()
pygame.init()

screen = pygame.display.set_mode((480, 248))
pygame.display.set_caption("Music Player")

# Specify the directory where your music files are stored
music_dir = r"C:\Users\user\Music"

# Check if the music directory exists
if not os.path.exists(music_dir):
    print("Error: Music directory does not exist.")
    pygame.quit()
    quit()

# Load all music files from the specified directory
songs = [os.path.join(music_dir, file) for file in os.listdir(music_dir) if file.endswith(".mp3")]

# Check if any music files are found
if not songs:
    print("Error: No MP3 files found in the music directory.")
    pygame.quit()
    quit()

current_music = 0

# Load and play the first song
pygame.mixer.music.load(songs[current_music])
pygame.mixer.music.play()

# Load background image
background = pygame.image.load(r"C:\Users\user\Downloads\player.png")
background_rect = background.get_rect()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play()
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
