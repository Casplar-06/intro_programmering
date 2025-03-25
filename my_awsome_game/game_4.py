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
    distance_squared = ((obj_1_x - obj_2_x) ** 2 + (obj_1_y - obj_2_y) ** 2)
    return distance_squared < (obj_1_radius + obj_2_radius) ** 2

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Screen setup
size = (400, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")

# Load images
snake_image = pygame.image.load("my_awsome_game/img/snake.png")
snake_x, snake_y = 200, 400
snake_radius = (snake_image.get_width() + snake_image.get_height()) / 4

plum_image = pygame.image.load("my_awsome_game/img/plum.png")
plum_radius = (plum_image.get_width() + plum_image.get_height()) / 4

cherries_image = pygame.image.load("my_awsome_game/img/cherries.png")
cherries_radius = (cherries_image.get_width() + cherries_image.get_height()) / 4

# Game variables
snake_speed = 5
snake_dx, snake_dy = 0, 0
score = 0

plums = {}
cherries = {}

clock = pygame.time.Clock()
is_running = True

# Main Loop
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # Snake movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake_dx, snake_dy = -snake_speed, 0
    elif keys[pygame.K_RIGHT]:
        snake_dx, snake_dy = snake_speed, 0
    elif keys[pygame.K_UP]:
        snake_dx, snake_dy = 0, -snake_speed
    elif keys[pygame.K_DOWN]:
        snake_dx, snake_dy = 0, snake_speed
    else:
        snake_dx, snake_dy = 0, 0
    
    snake_x += snake_dx
    snake_y += snake_dy
    
    # Wrap the snake around the screen
    snake_x %= 400
    snake_y %= 500

    # Spawn plums
    if random.randint(0, 100) < 2:
        plum_id = len(plums)
        plums[plum_id] = {"x": random.randint(0, 400), "y": 0, "speed": 1}
    
    # Spawn deadly fruit
    if random.randint(0, 200) < 1:
        fruit_id = len(cherries)
        cherries[fruit_id] = {"x": random.randint(0, 400), "y": 0, "speed": 1}
    
    # Move plums
    to_remove = []
    for plum_id, plum in plums.items():
        plum["y"] += plum["speed"]
        plum["speed"] += 0.2
        if plum["y"] > 500:
            to_remove.append(plum_id)
        elif collides(snake_x, snake_y, snake_radius, plum["x"], plum["y"], plum_radius):
            to_remove.append(plum_id)
            score += 1
    for plum_id in to_remove:
        del plums[plum_id]
    
    # Move deadly fruits
    to_remove = []
    for fruit_id, fruit in cherries.items():
        fruit["y"] += fruit["speed"]
        fruit["speed"] += 0.2
        if fruit["y"] > 500:
            to_remove.append(fruit_id)
        elif collides(snake_x, snake_y, snake_radius, fruit["x"], fruit["y"], cherries_radius):
            print("Game Over!")
            is_running = False
    for fruit_id in to_remove:
        del cherries[fruit_id]
    
    # Drawing
    screen.fill(GREEN)
    screen.blit(snake_image, (snake_x, snake_y))
    for plum in plums.values():
        screen.blit(plum_image, (plum["x"], plum["y"]))
    for fruit in cherries.values():
        screen.blit(cherries_image, (fruit["x"], fruit["y"]))
    
    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()