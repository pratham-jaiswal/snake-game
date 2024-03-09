import pygame
import random
import sys

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

WHITE = (255, 255, 255)
BG = (32, 32, 32)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

block_size = 20
snake_speed = 7

score = 0

font_name = pygame.font.match_font('Arial')
font = pygame.font.Font(font_name, 30)

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.circle(screen, GREEN, (block[0], block[1]), block_size // 2)

def message(msg, color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [width / 6, height / 3])

def show_score(score):
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, [10, 10])

def gameLoop():
    global score    
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, width - block_size * 2) / block_size) * block_size
    food_y = round(random.randrange(0, height - block_size * 2) / block_size) * block_size

    while not game_over:

        while game_close == True:
            screen.fill(BG)
            show_score(score)
            message("You lost! Press Q-Quit or R-Restart", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        score = 0
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        
        x += x_change
        y += y_change
        screen.fill(BG)
        pygame.draw.circle(screen, RED, (food_x, food_y), block_size // 2)

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_list)
        show_score(score)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size * 2) / block_size) * block_size
            food_y = round(random.randrange(0, height - block_size * 2) / block_size) * block_size
            snake_length += 1
            score += 1

        while (food_x, food_y) in snake_list:
            food_x = round(random.randrange(0, width - block_size * 2) / block_size) * block_size
            food_y = round(random.randrange(0, height - block_size * 2) / block_size) * block_size

        pygame.display.update()

        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    sys.exit()

gameLoop()