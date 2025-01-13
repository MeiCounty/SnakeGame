import pygame
import time
import random

# 初始化Pygame
pygame.init()

# 游戏窗口设置
WIDTH, HEIGHT = 600, 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇")

# 颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)

# 时钟和字体
clock = pygame.time.Clock()
snake_speed = 15
font_style = pygame.font.SysFont("bahnschrift", 25)

# 贪吃蛇初始化
snake_block = 10
snake_list = []
snake_length = 1

# 显示分数
def display_score(score):
    value = font_style.render("Your Score: " + str(score), True, RED)
    window.blit(value, [0, 0])

# 绘制蛇
def draw_snake(block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, GREEN, [x[0], x[1], block, block])

# 游戏结束信息
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [WIDTH / 6, HEIGHT / 3])

# 游戏主循环
def game_loop():
    global snake_length, snake_list
    game_over = False
    game_close = False

    x, y = WIDTH / 2, HEIGHT / 2
    x_change, y_change = 0, 0

    food_x = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            window.fill(BLACK)
            message("You lost! Press Q-Quit or C-Play Again", RED)
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True
        x += x_change
        y += y_change
        window.fill(BLACK)
        pygame.draw.rect(window, WHITE, [food_x, food_y, snake_block, snake_block])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        display_score(snake_length - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()