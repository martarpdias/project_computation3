import pygame
import math
from config import *
from utils import *

class Projectile1(pygame.sprite.Sprite):
    def __init__(self, x:int , y:int , direction:float):
        super().__init__()
        self.radius = projectile_size
        self.color = yellow
        self.rect = pygame.Rect(x - self.radius, y - self.radius, self.radius * 2, self.radius * 2) #x, y, width, height
        self.speed = 7
        self.direction = direction

    def update(self):
        self.rect.x += int(self.speed * math.cos(self.direction))
        self.rect.y += int(self.speed * math.sin(self.direction))

        if self.rect.x < 0 or self.rect.x > width or self.rect.y < 0 or self.rect.y > height:
            self.kill()

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius)
