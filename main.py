from pygame import *
from button import Button
from sprite import Player, GameSprite, Wall
from random import randint
bg = transform.scale(image.load("bg.png"), (700,500))
bg_width = bg.get_width()
bg_height = bg.get_height()
tiles = 2 
scroll = 0

window = display.set_mode((700,500))

game = True
run = False
clock = time.Clock()

btn1 = Button('start_btn.png', 100,100, 100, 50)
btn2 = Button('exit_btn.png', 300,100, 100, 50)

player = Player('mario_standing.png','mario_right.png', 50,75 , 100,200)
money = GameSprite('jump.png',50,50 , 200,200)
speed = 0

wall = Wall(200,50, 0,0, transperancy=0)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                run = False
            if e.key == K_LEFT:
                scroll -= 5
            if e.key == K_SPACE:
                player.isJump = True
  
    if run:
    
        window.blit(bg, (0,0))
        player.draw(window)
        player.move()
        player.jump()
        money.draw(window)

        wall.draw(window)

        money.rect.x += speed
        if money.rect.x >500:
            speed *= -1
        if money.rect.x < 0:
            speed *= -1
        if wall.rect.colliderect(player.rect):
            speed = 5
    else:
        window.fill((0,0,0))
        if btn1.draw(window):
            run = True
        if btn2.draw(window):
            game = False
    
   
    display.update()
    clock.tick(60)