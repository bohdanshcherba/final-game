from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self, img_name, width, height, x, y):
        self.image = transform.scale(image.load(img_name), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def __init__(self, img_name_1, img_name_2, width, height, x, y):
        super().__init__(img_name_1, width, height, x, y)
        self.img_1 = transform.scale(image.load(img_name_1), (width, height))
        self.img_2 = transform.scale(image.load(img_name_2), (width, height))

        self.isJump = False
        self.jumpCount = 10

    def move(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.image = self.img_2
            self.rect.x -= 5
        if keys[K_RIGHT]:
            self.image = self.img_1
            self.rect.x += 5

    def jump(self):
        if self.isJump:
            if self.jumpCount >= -10: 
                self.rect.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10



    def fire(self):
        if self.image == self.img_1:
            bullet = Bullet(self.rect.centerx, self.rect.centery, "right")
        else:
            bullet = Bullet(self.rect.centerx, self.rect.centery, "left")
        return bullet

class Bullet(sprite.Sprite):
    def __init__(self, x,y, direction ):
        self.bull = Surface((20,20))
        self.bull.fill((255,0,0))
        self.rect = self.bull.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction
        self.speed = 5

    def update(self, window):
        if self.direction == "right":
            self.rect.x += self.speed
        if self.direction == "left":
            self.rect.x -= self.speed
     

        window.blit(self.bull, (self.rect.x, self.rect.y))



class Wall(GameSprite):
    def __init__(self, width,height, x,y, color=(255,255,255), transperancy=255):
        self.wall = Surface((width,height))
        self.wall.set_alpha(transperancy)
        self.wall.fill(color)
        self.rect = self.wall.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, window):
        self.rect.x -= 5
        if self.rect.x < 0:
            self.rect.x = 700
            self.rect.y = randint(50, 300)


        window.blit(self.wall, (self.rect.x, self.rect.y))

    def draw_wall(self, window):
        window.blit(self.wall, (self.rect.x, self.rect.y))
