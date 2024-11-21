import pygame

class Player(object):
    def __init__(self, x, y, width, height, walkRight, walkLeft, still):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.distance = 5
        self.jumpping = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.walkRight = walkRight
        self.walkLeft = walkLeft
        self.still = still
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)   


    def draw(self, screen):
        if self.walkCount + 1 >= 27: # 9 images * 3
            self.walkCount = 0

        # Display walking animation
        if not self.standing:
            if self.left:
                screen.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                screen.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                screen.blit(self.walkRight[0], (self.x, self.y))
            else:
                screen.blit(self.walkLeft[0], (self.x, self.y))

        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        #pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)
        

