from config import *
import math
import pygame
from classProjectile import Projectile1
from classPlayer import Player1
from classEnemy import Enemy1

def execute_game():
    """
    Main function to execute the game loop

    """
    #clock for controlling the frame rate
    clock = pygame.time.Clock()

    #setting up the background
    screen = pygame.display.set_mode((resolution))
    background = pygame.image.load('game_project/pics/bg.webp')
    background = pygame.transform.scale(background,(width,height))



    #player setup
    player=Player1()
    player_group=pygame.sprite.Group()
    player_group.add(player)

     #Initialize bullets
    bullets=pygame.sprite.Group()

    #initialize the enemy group
    enemies=pygame.sprite.Group()
    enemy_spawn_timer=0


    running=True
    while running:
        #control the frame rate
        clock.tick(fps)
        #fill the background
        screen.blit(background,(0,0))

        #event handling
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()

        #shooting
        player.shoot(bullets)
        
        #spawning the enemies
        if enemy_spawn_timer<=0:
            new_enemy=Enemy1()
            enemies.add(new_enemy)
            enemy_spawn_timer=fps*2 #every two seconds

        # Checking for collision between
        for bullet in bullets:
            collided_enemies = pygame.sprite.spritecollide(bullet, enemies, False)
            for enemy in collided_enemies:
                enemy.health -= 5  # decrease health by 5 , for example
                bullet.kill()  # destroy the bullet
                if enemy.health <= 0:
                    enemy.kill()  # destroy the enemy

        #update positions
        player_group.update()
        bullets.update()
        enemies.update(player)


        #update the enemy spawn timer
        enemy_spawn_timer -= 1

         #drawing the objects
        player_group.draw(screen)
        enemies.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)


        pygame.display.flip()

