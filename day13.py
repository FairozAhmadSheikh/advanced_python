import pygame
import random
import math

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Load assets
player_img = pygame.image.load("player.png")
enemy_img = pygame.image.load("enemy.png")
bullet_img = pygame.image.load("bullet.png")

# Player class
class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 80
        self.speed = 5
        self.bullets = []

    def move(self, direction):
        self.x += direction * self.speed
        self.x = max(0, min(WIDTH - 64, self.x))

    def shoot(self):
        self.bullets.append(Bullet(self.x + 16, self.y))

    def draw(self):
        screen.blit(player_img, (self.x, self.y))
        for bullet in self.bullets:
            bullet.draw()
# Enemy class
class Enemy:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 64)
        self.y = random.randint(50, 150)
        self.speed = 3
        self.direction = 1

    def move(self):
        self.x += self.speed * self.direction
        if self.x <= 0 or self.x >= WIDTH - 64:
            self.direction *= -1
            self.y += 40

    def draw(self):
        screen.blit(enemy_img, (self.x, self.y))