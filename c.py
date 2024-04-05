import pygame
import math

# Initialize Pygame
pygame.init()

# Set the width and height of the screen (window)
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Analog Clock")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define clock parameters
clock_radius = min(width, height) // 3
minute_hand_length = clock_radius * 3 // 4
second_hand_length = clock_radius - 10

# Define font
font = pygame.font.Font(None, 24)

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Get current time
    current_time = pygame.time.get_ticks() // 1000  # Get elapsed time in seconds
    hour = current_time // 3600 % 12
    minute = (current_time // 60) % 60
    second = current_time % 60

    # Draw clock face
    pygame.draw.circle(screen, BLACK, (width // 2, height // 2), clock_radius, 2)

    # Draw numbers
    for num in range(1, 13):
        angle = math.radians(90 - num * 30)  # Adjust the angle calculation for clockwise direction
        num_x = width // 2 + int(math.cos(angle) * clock_radius * 0.85)
        num_y = height // 2 - int(math.sin(angle) * clock_radius * 0.85)
        number_text = font.render(str(num), True, BLACK)
        num_rect = number_text.get_rect(center=(num_x, num_y))
        screen.blit(number_text, num_rect)

    # Draw minute hand
    minute_angle = math.radians((minute + second / 60) * 6)  # adjusted for seconds
    minute_hand_x = width // 2 + int(math.cos(minute_angle) * minute_hand_length)
    minute_hand_y = height // 2 - int(math.sin(minute_angle) * minute_hand_length)
    pygame.draw.line(screen, BLACK, (width // 2, height // 2), (minute_hand_x, minute_hand_y), 3)

    # Draw second hand
    second_angle = math.radians(second * 6)
    second_hand_x = width // 2 + int(math.cos(second_angle) * second_hand_length)
    second_hand_y = height // 2 - int(math.sin(second_angle) * second_hand_length)
    pygame.draw.line(screen, BLACK, (width // 2, height // 2), (second_hand_x, second_hand_y), 1)

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
