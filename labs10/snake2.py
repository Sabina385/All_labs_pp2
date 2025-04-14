import pygame
import time
import random
import psycopg2
import sys

pygame.init()

# Colors
orange = (255, 123, 7)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
white = (255, 255, 255)

# Screen dimensions
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# Snake and Food dimensions, speed
snake_block = 20
snake_speed = 9

# Connect to PostgreSQL database
def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="snakegame", user="postgres", password="109115", host="localhost"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        sys.exit(1)

# Create user and user_score tables if they don't exist
def create_tables():
    conn = connect_db()
    c = conn.cursor()
    
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            level INT DEFAULT 1,
            score INT DEFAULT 0
        );
    """)
    conn.commit()
    c.close()
    conn.close()

# Get or create a user
def get_or_create_user(username):
    conn = connect_db()
    c = conn.cursor()
    
    c.execute("SELECT id, level, score FROM users WHERE username = %s", (username,))
    user = c.fetchone()
    
    if user is None:
        # User doesn't exist, create a new one
        c.execute("INSERT INTO users (username) VALUES (%s) RETURNING id, level, score", (username,))
        user = c.fetchone()
        conn.commit()
    
    c.close()
    conn.close()
    
    return user

# Save game state
def save_game_state(user_id, score, level):
    conn = connect_db()
    c = conn.cursor()
    
    c.execute("UPDATE users SET score = %s, level = %s WHERE id = %s", (score, level, user_id))
    conn.commit()
    
    c.close()
    conn.close()

# Food class to handle different types of food
class Food:
    def __init__(self):
        self.respawn()

    def respawn(self):
        self.x = round(random.randrange(0, screen_width - snake_block) / snake_block) * snake_block
        self.y = round(random.randrange(0, screen_height - snake_block) / snake_block) * snake_block
        self.size = random.choice([17, 20, 24])
        self.points = 5 if self.size == 17 else 3 if self.size == 20 else 1
        self.timer = time.time() + random.randint(10, 20)

    def draw(self):
        pygame.draw.rect(screen, green if self.size == 10 else blue if self.size == 15 else red, [self.x, self.y, self.size, self.size])
        font = pygame.font.Font(None, 24)
        text = font.render(str(self.points), True, white)
        text_rect = text.get_rect(center=(self.x + self.size / 2, self.y + self.size / 2))
        screen.blit(text, text_rect)

# Function to draw the snake
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, orange, [x[0], x[1], snake_block, snake_block])

# Main game function
def snakegame():
    username = input("Enter your username: ")
    user_id, level, score = get_or_create_user(username)
    print(f"Welcome {username}! Current level: {level}, Current score: {score}")
    
    game_over = False
    game_end = False
    paused = False  # Flag for pausing the game
    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    Length_of_snake = 1
    food = Food()

    while not game_over:
        while game_end:
            font = pygame.font.Font(None, 36)
            text = font.render(f"You Lost! Score: {score}", True, red)
            screen.blit(text, [screen_width / 4, screen_height / 3])

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_end = False

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
                elif event.key == pygame.K_p:  # Toggle pause
                    paused = not paused

        if paused:
            font = pygame.font.Font(None, 36)
            text = font.render("PAUSED. Press any key to continue.", True, red)
            screen.blit(text, [screen_width / 4, screen_height / 3])
            pygame.display.update()
            continue  # Skip game update while paused

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_end = True

        x1 += x1_change
        y1 += y1_change

        screen.fill(black)
        
        food.draw()

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

        if x1 == food.x and y1 == food.y:
            score += food.points
            Length_of_snake += 1
            food.respawn()

        if time.time() > food.timer:
            food.respawn()

        clock.tick(snake_speed)

        # Save game state
        save_game_state(user_id, score, level)

    pygame.quit()
    quit()

if __name__ == "__main__":
    create_tables()  # Create the necessary tables if they don't exist
    snakegame()

