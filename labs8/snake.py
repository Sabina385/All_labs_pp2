import pygame
import time
import random
import sys

pygame.init()

orange = (255, 123, 7)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Screen dimensions
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# Snake and Food dimensions, speed
snake_block = 20  # Increased from 10 to 20
snake_speed = 9 # Adjusted speed for larger blocks
snake_list = []

def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, orange, [x[0], x[1], snake_block, snake_block])

def snakegame():
    game_over = False
    game_end = False
    # Snake coordinates
    x1 = screen_width / 2 # Centered snake
    y1 = screen_height / 2
    # Snake movement
    x1_change = 0
    y1_change = 0

    snake_list = []
    Length_of_snake = 1
    score = 0 # Initialize the score


    foodx = round(random.randrange(0, screen_width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, screen_height - snake_block) / snake_block) * snake_block
    while not game_over:
        while game_end == True:
            #score = Length_of_snake - 1 # Score is now updated during the game
            font = pygame.font.Font(None, 36)
            text = font.render(f"You Lost! Score: {score}", True, red) # Display loss screen
            screen.blit(text, [screen_width/4, screen_height/3])

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

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_end = True

        x1 += x1_change
        y1 += y1_change

        screen.fill(black)
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)

        if len(snake_list) > Length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_Head:
                game_end = True

        snake(snake_block, snake_list)

        font = pygame.font.Font(None, 36) # Score during the game
        score_text = font.render(f"Score: {score}", True, green)
        screen.blit(score_text, [10, 10]) # Position top left

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, screen_height - snake_block) / snake_block) * snake_block
            Length_of_snake += 1
            score +=1 # Increased after food
        clock.tick(snake_speed)

    pygame.quit()
    quit()

snakegame()
                       
        
                      
                     
                      
        
  
            
            
