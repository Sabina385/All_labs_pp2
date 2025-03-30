import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

road_img = pygame.image.load("AnimatedStreet.png")
road_img = pygame.transform.scale(road_img, (WIDTH, HEIGHT))

road_y = 0 #начальная позиции
road_speed = 5 #скорость

class Car:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 150
        self.speed = 9
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (50, 100))

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 50:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - 50:
            self.x += self.speed

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


class Coin:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = random.randint(-150, -50)
        self.speed = road_speed
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))

    def move(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.__init__()

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


class Enemy:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = -100
        self.speed = 10
        self.image = pygame.image.load("Enemy.png")
        self.image = pygame.transform.scale(self.image, (50, 100))

    def move(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = -100
            self.x = random.randint(50, WIDTH - 50)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


def check_collision(player, enemy):
    return (player.x < enemy.x + 50 and
            player.x + 50 > enemy.x and
            player.y < enemy.y + 100 and
            player.y + 100 > enemy.y)

player = Car()
coins = [Coin()]
enemy = Enemy()
score = 0
game_over = False  


running = True
while running:
    keys = pygame.key.get_pressed()

    if not game_over:  
        road_y += road_speed
        if road_y >= HEIGHT:
            road_y = 0

        screen.blit(road_img, (0, road_y - HEIGHT))
        screen.blit(road_img, (0, road_y))

        player.move(keys)
        player.draw()

        
        for coin in coins:
            coin.move()
            coin.draw()
            if player.x < coin.x < player.x + 50 and player.y < coin.y < player.y + 100:
                score += 1
                coins.remove(coin)
                coins.append(Coin())

    
        enemy.move()
        enemy.draw()

        # Проверяем столкновение с врагом
        if check_collision(player, enemy):
            game_over = True  


        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(text, (WIDTH - 120, 20))
    else:
        font = pygame.font.Font(None, 72)
        text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
        pygame.display.update()
        pygame.time.delay(2000) 
        running = False  # Закрываем игру

    pygame.display.update()
    clock.tick(30)

    # Проверка выхода
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
                      
        