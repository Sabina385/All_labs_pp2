import pygame 
import time 
import random 
import sys

pygame.init()

# Цвета
orange = (255, 123, 7) 
black = (0, 0, 0) 
red = (213, 50, 80) 
green = (0, 255, 0) 
blue = (50, 153, 213)

# Параметры экрана
screen_width = 600 
screen_height = 400 
screen = pygame.display.set_mode((screen_width, screen_height)) 
pygame.display.set_caption("Snake") 
clock = pygame.time.Clock()

# Размер блока змеи
snake_block = 20  
snake_speed = 9  # Скорость

# Функция для рисования змеи
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, orange, [x[0], x[1], snake_block, snake_block])

# Класс для еды
class Food: 
    def __init__(self): 
        self.respawn()

    def respawn(self):
        self.x = round(random.randrange(0, screen_width - snake_block) / snake_block) * snake_block
        self.y = round(random.randrange(0, screen_height - snake_block) / snake_block) * snake_block
        self.weight = random.choice([(5, green, 10), (3, blue, 15), (1, red, 20)])  # (баллы, цвет, размер)
        self.timer = time.time() + random.randint(15, 25)  # Исчезает через 15-25 сек

    def draw(self):
        pygame.draw.rect(screen, self.weight[1], [self.x, self.y, self.weight[2], self.weight[2]])

food = Food()

# Главная игровая функция
def snakegame(): 
    game_over = False
    game_end = False

    # Начальные координаты змеи
    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    Length_of_snake = 1
    score = 0  # Начальный счет

    while not game_over:
        while game_end:
            font = pygame.font.Font(None, 36)
            text = font.render(f"You Lost! Score: {score}", True, red)
            screen.blit(text, [screen_width/4, screen_height/3])
            pygame.display.update()
            time.sleep(2)  # Задержка 2 секунды перед выходом из игры

            # Прерываем игровой цикл и завершаем игру
            game_over = True
            game_end = False

        # Обработка событий (управление змейкой)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Проверка выхода за границы экрана
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_end = True

        x1 += x1_change
        y1 += y1_change

        screen.fill(black)
        food.draw()

        # Логика движения змеи
        snake_Head = [x1, y1]
        snake_list.append(snake_Head)

        if len(snake_list) > Length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_Head:
                game_end = True

        snake(snake_block, snake_list)

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, green)
        screen.blit(score_text, [10, 10])

        pygame.display.update()
        
        # Проверка на столкновение с едой
        if x1 == food.x and y1 == food.y:
            score += food.weight[0]  # Увеличиваем счет
            Length_of_snake += 1  # Увеличиваем длину змеи
            food.respawn()

        # Проверка времени для исчезновения еды
        if time.time() > food.timer:
            food.respawn()

        clock.tick(snake_speed)

pygame.quit()
quit()

snakegame()
