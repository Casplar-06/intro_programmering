'''
Task

Make the circle stay inside of the window.
'''

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Draw circle")

# Add visual elements to the game
circle_x = 50
circle_y = 50
circle_radius = 25
circle_speed_x = 2
circle_speed_y = 1

# Loop until the user clicks the close button.
is_running = True

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while is_running:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # --- Game logic should go here
    circle_x += circle_speed_x
    circle_y += circle_speed_y

    # Bounce off the edges
    if circle_x - circle_radius <= 0 or circle_x + circle_radius >= size[0]:
        circle_speed_x *= -1
    if circle_y - circle_radius <= 0 or circle_y + circle_radius >= size[1]:
        circle_speed_y *= -1

    # --- Screen-clearing code goes here
    screen.fill(BLACK)

    # --- Drawing code should go here
    pygame.draw.circle(screen, RED, [circle_x, circle_y], circle_radius)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(100)

# Close the window and quit.
pygame.quit()