'''
Uses dictionary insted of list to store each plum.


Tasks

1. Make the snake move properly.
2. Add score. Display the score on the screen.
3. Add an other fruit, that will kill the snake.

'''
 
import pygame
import random

def collides(obj_1_x, obj_1_y, obj_1_radius, obj_2_x, obj_2_y, obj_2_radius):
    ''' Check if two objects collide. Circular collision detection.
    '''
    distance_squared = ((obj_1_x - obj_2_x) ** 2 + (obj_1_y - obj_2_y) ** 2)
    return distance_squared < (obj_1_radius + obj_2_radius) ** 2

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (400, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")

# Add visual elements to the game
snake_image = pygame.image.load("my_awsome_game/img/snake.png")
snake_x = 50
snake_y = 400
snake_last_direction = "right"
snake_radius = (snake_image.get_width() + snake_image.get_height()) / 4

plum_image = pygame.image.load("my_awsome_game/img/plum.png")
plums = []
plum_radius = (plum_image.get_width() + plum_image.get_height()) / 4
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Loop until the user clicks the close button.
is_running = True

# -------- Main Program Loop -----------
while is_running:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
 
    # --- Game logic should go here
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake_x -= 5
        if (snake_last_direction == "right"):
            snake_image = pygame.transform.flip(snake_image, True, False)
            snake_last_direction = "left"
        # Wrap the snake around the screen.
        if snake_x < 0:
            snake_x = 600

    # plums
    # Chance of having a new plum.
    if (random.randint(0, 100) < 2):
        plum_x = random.randint(0, 600)
        # Add plum coodinates to the list.
        plum = {}
        plum['x'] = plum_x
        plum['y'] = 0
        plum['speed'] = 0
        plums.append(plum) # x, y, speed
    
    # move plums
    for plum in plums:
        # Move the plum down.
        plum['y'] += plum['speed']
        # Increase the speed of the plum.
        plum['speed'] += 0.2
        # Remove plums that have gone off the screen.
        if plum['y'] > 800:
            plums.remove(plum)
        # Check for collisions with the snake.
        if collides(snake_x, snake_y, snake_radius, 
                    plum['x'], plum['y'], plum_radius):
            plums.remove(plum)
            print("Yum!")
        

        
    
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREEN)
 
    # --- Drawing code should go here
    screen.blit(snake_image, [snake_x, snake_y])
    for plum in plums:
        screen.blit(plum_image, [plum['x'], plum['y']])
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Clean up when the game exits.
pygame.quit()