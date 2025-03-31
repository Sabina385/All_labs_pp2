import pygame
import time
import random
import sys

pygame.init()

# Colors
orange = (255, 123, 7)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
white = (255, 255, 255)  # Белый цвет для текста

# Screen dimensions
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# Snake and Food dimensions, speed
snake_block = 20  # Increased from 10 to 20
snake_speed = 9  # Adjusted speed for larger blocks

# Food class to handle different types of food
class Food:
    def __init__(self):
        self.respawn()

    def respawn(self):
        self.x = round(random.randrange(0, screen_width - snake_block) / snake_block) * snake_block
        self.y = round(random.randrange(0, screen_height - snake_block) / snake_block) * snake_block
        self.size = random.choice([10, 15, 20])  # Random food size
        self.points = 1 if self.size == 10 else 3 if self.size == 15 else 5  # Points based on food size
        self.timer = time.time() + random.randint(10, 20)  # Food disappears in 10-20 seconds

    def draw(self):
        # Draw food (color depends on size)
        pygame.draw.rect(screen, green if self.size == 10 else blue if self.size == 15 else red,
                         [self.x, self.y, self.size, self.size])
        
        # Draw points text on the food
        font = pygame.font.Font(None, 24)
        text = font.render(str(self.points), True, white)  # White color for text
        # Position text at the center of the food
        text_rect = text.get_rect(center=(self.x + self.size / 2, self.y + self.size / 2))
        screen.blit(text, text_rect)

# Function to draw the snake
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, orange, [x[0], x[1], snake_block, snake_block])

# Main game function
def snakegame():
    game_over = False
    game_end = False
    # Snake coordinates
    x1 = screen_width / 2  # Centered snake
    y1 = screen_height / 2
    # Snake movement
    x1_change = 0
    y1_change = 0

    snake_list = []
    Length_of_snake = 1
    score = 0  # Initialize the score

    food = Food()  # Create a food object
    while not game_over:
        while game_end:
            font = pygame.font.Font(None, 36)
            text = font.render(f"You Lost! Score: {score}", True, red)  # Display loss screen
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

        # Check if snake hits boundaries
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_end = True

        # Update snake position
        x1 += x1_change
        y1 += y1_change

        # Fill screen with black (background color)
        screen.fill(black)
        
        # Draw food
        food.draw()

        # Snake logic
        snake_Head = [x1, y1]
        snake_list.append(snake_Head)

        if len(snake_list) > Length_of_snake:
            del snake_list[0]

        # Check if snake collides with itself
        for x in snake_list[:-1]:
            if x == snake_Head:
                game_end = True

        snake(snake_block, snake_list)

        # Display score
        font = pygame.font.Font(None, 36)  # Score during the game
        score_text = font.render(f"Score: {score}", True, green)
        screen.blit(score_text, [10, 10])  # Position top left

        pygame.display.update()

        # Check if snake eats food
        if x1 == food.x and y1 == food.y:
            score += food.points  # Increase score based on food points
            Length_of_snake += 1  # Increase snake length
            food.respawn()  # Respawn food

        # Check if food timer expired, if so respawn food
        if time.time() > food.timer:
            food.respawn()

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
if __name__ == "__main__":
    snakegame()





    