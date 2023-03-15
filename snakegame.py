import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
WINDOW_TITLE = 'RangaMan Snake Game'
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

# Set up the game clock
clock = pygame.time.Clock()

# Set up the snake and food
SNAKE_SIZE = 10
snake_head = [WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2]
snake_body = [snake_head]
snake_direction = 'RIGHT'
food_position = [random.randrange(0, WINDOW_WIDTH - SNAKE_SIZE, SNAKE_SIZE),
                 random.randrange(0, WINDOW_HEIGHT - SNAKE_SIZE, SNAKE_SIZE)]

# Set up the game loop
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != 'DOWN':
                snake_direction = 'UP'
            elif event.key == pygame.K_DOWN and snake_direction != 'UP':
                snake_direction = 'DOWN'
            elif event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                snake_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                snake_direction = 'RIGHT'

    # Move the snake
    if snake_direction == 'UP':
        snake_head[1] -= SNAKE_SIZE
    elif snake_direction == 'DOWN':
        snake_head[1] += SNAKE_SIZE
    elif snake_direction == 'LEFT':
        snake_head[0] -= SNAKE_SIZE
    elif snake_direction == 'RIGHT':
        snake_head[0] += SNAKE_SIZE

    # Check for collision with the food
    if snake_head == food_position:
        food_position = [random.randrange(0, WINDOW_WIDTH - SNAKE_SIZE, SNAKE_SIZE),
                         random.randrange(0, WINDOW_HEIGHT - SNAKE_SIZE, SNAKE_SIZE)]
        snake_body.append(snake_body[-1][:])

    # Update the snake's body
    snake_body.insert(0, snake_head[:])
    snake_body.pop()

    # Check for collision with the walls
    if snake_head[0] < 0 or snake_head[0] >= WINDOW_WIDTH or \
            snake_head[1] < 0 or snake_head[1] >= WINDOW_HEIGHT:
        game_over = True

    # Check for collision with the snake's body
    for body_part in snake_body[1:]:
        if snake_head == body_part:
            game_over = True

    # Draw the game objects
    window.fill((255, 255, 255))
    pygame.draw.rect(window, (255, 0, 0), [food_position[0], food_position[1], SNAKE_SIZE, SNAKE_SIZE])
    for body_part in snake_body:
        pygame.draw.rect(window, (0, 255, 0), [body_part[0], body_part[1], SNAKE_SIZE, SNAKE_SIZE])
    pygame.display.update()

    # Tick the clock
    clock.tick(10)

# Quit Pygame
pygame.quit()