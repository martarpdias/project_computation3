import pygame

class Enemy(object):
    walkRight = [pygame.image.load(f'game_project/pics/R{i}E.png') for i in range(1, 12)]
    walkLeft = [pygame.image.load(f'game_project/pics/L{i}E.png') for i in range(1, 12)]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33: # 11 images *3
            self.walkCount = 0

        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y)) # 3 is the speed of the animation
            self.walkCount += 1 
        else:
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        
        

        


    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        print('hit')