

import pygame
import time
import random
import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="snakegame",
    user="postgres",
    password="109115",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Создание таблиц, если они ещё не существуют
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) UNIQUE NOT NULL,
        level INTEGER DEFAULT 1
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS scores (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        username VARCHAR(100),
        score INTEGER,
        level INTEGER,
        played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()

# Ввод имени пользователя
username = input("Введите имя пользователя: ")

cursor.execute("SELECT id, level FROM users WHERE username = %s", (username,))
user = cursor.fetchone()

if user:
    user_id, level = user
    print(f"Добро пожаловать, {username}. Ваш текущий уровень: {level}")
else:
    cursor.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cursor.fetchone()[0]
    level = 1
    conn.commit()
    print(f"Создан новый пользователь: {username}")

# Настройка Pygame
pygame.init()
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

snake_block = 20

# Цвета
orange = (255, 123, 7)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
white = (255, 255, 255)

# Класс еды
class Food:
    def __init__(self):
        self.respawn()

    def respawn(self):
        self.x = round(random.randrange(0, screen_width - snake_block) / snake_block) * snake_block
        self.y = round(random.randrange(0, screen_height - snake_block) / snake_block) * snake_block
        self.size = random.choice([14, 18, 22])
        self.points = 1 if self.size == 22 else 2 if self.size == 18 else 3
        self.timer = time.time() + random.randint(10, 20)

    def draw(self):
        pygame.draw.rect(screen, green if self.size == 14 else blue if self.size == 18 else red,
                         [self.x, self.y, self.size, self.size])
        font = pygame.font.Font(None, 24)
        text = font.render(str(self.points), True, white)
        text_rect = text.get_rect(center=(self.x + self.size / 2, self.y + self.size / 2))
        screen.blit(text, text_rect)

# Функция отрисовки змейки
def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, orange, [x[0], x[1], snake_block, snake_block])

# Сохранение результата
def save_score(user_id, username, score, level):
    cursor.execute("INSERT INTO scores (user_id, username, score, level) VALUES (%s, %s, %s, %s)",
                   (user_id, username, score, level))
    cursor.execute("UPDATE users SET level = %s WHERE id = %s", (level, user_id))
    conn.commit()

# Основная функция игры
def snake_game():
    x = screen_width // 2
    y = screen_height // 2
    dx = 0
    dy = 0
    snake = []
    length = 1
    score = 0
    game_over = False
    paused = False
    food = Food()

    global level
    snake_speed = 10 + (level - 1)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_score(user_id, username, score, level)
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx, dy = -snake_block, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = snake_block, 0
                elif event.key == pygame.K_UP:
                    dx, dy = 0, -snake_block
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, snake_block
                elif event.key == pygame.K_p:
                    paused = not paused
                    if paused:
                        save_score(user_id, username, score, level)

        if paused:
            continue

        x += dx
        y += dy

        if x < 0 or x >= screen_width or y < 0 or y >= screen_height:
            save_score(user_id, username, score, level)
            game_over = True

        screen.fill(black)
        food.draw()

        head = [x, y]
        snake.append(head)
        if len(snake) > length:
            del snake[0]

        for part in snake[:-1]:
            if part == head:
                save_score(user_id, username, score, level)
                game_over = True

        draw_snake(snake)

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}  Level: {level}", True, white)
        screen.blit(score_text, [10, 10])

        pygame.display.update()

        if x == food.x and y == food.y:
            score += food.points
            length += 1
            food.respawn()

            if score // 12 + 1 > level:
                level = score // 12 + 1
                snake_speed = 10 + (level - 1)

        if time.time() > food.timer:
            food.respawn()

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Запуск игры
snake_game()








