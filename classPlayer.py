from config import *
import math
import pygame
from classProjectile import Projectile1

class Player1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 100))
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)

        #Game Play Variables
        self.speed = 5
        self.angle = 0 
        self.projectile_cooldown = 0  

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.bottom < height:
            self.rect.y += self.speed
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
 
    def shoot(self, projectiles: pygame.sprite.Group):
        if self.projectile_cooldown <= 0:
            for angle in [0, math.pi/2, math.pi, 3*math.pi/2]:
                projectile = Projectile1(self.rect.center[0], self.rect.center[1], angle)
                projectiles.add(projectile)
                self.projectile_cooldown = 10
            self.projectile_cooldown = fps
        self.projectile_cooldown -= 1