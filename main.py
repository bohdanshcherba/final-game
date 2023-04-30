from pygame import *
from button import Button
from sprite import Player, GameSprite, Wall
from random import randint

tiles = 2 
scroll = 0

window = display.set_mode((700,500))
WINDOW_WIDTH, WINDOW_HEIGHT = display.get_surface().get_size()
bg = transform.scale(image.load("bg.png"), (WINDOW_WIDTH,WINDOW_HEIGHT))
bg_width = bg.get_width()
bg_height = bg.get_height()

game = True
run = True
clock = time.Clock()

btn1 = Button('start_btn.png',  int(WINDOW_HEIGHT/2),int(WINDOW_WIDTH/2), 100, 50)
btn2 = Button('exit_btn.png', 300,100, 100, 50)

player = Player('mario_standing.png','mario_right.png', int(WINDOW_HEIGHT/5),int(WINDOW_WIDTH/5) , 100,200)
money = GameSprite('jump.png',50,50 , 200,200)
speed = 0

ground = Wall(WINDOW_WIDTH, 70, 0, WINDOW_HEIGHT-70, color=(0,2,20))

bullets = []
walls = []
for i in range(3):
    wall = Wall(100,10, randint(650,1500),randint(100, 400), color=(255,0,0))
    walls.append(wall)


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
            if e.key == K_RSHIFT:
                bullets.append(player.fire())
  
    if run:
    
        for i in range(0, tiles):
            window.blit(bg, (i * bg_width + scroll, 0))
    
        if abs(scroll) > bg_width:
            scroll = 0
        scroll -= 5
        player.draw(window)
        player.move()
        player.jump()
        player.rect.y += 3.2
        if player.rect.colliderect(ground.rect):
            player.rect.bottom = ground.rect.top
            

        ground.draw_wall(window)

        for b in bullets:
            b.update(window)
        


      
    else:
        window.fill((0,0,0))
        if btn1.draw(window):
            run = True
        if btn2.draw(window):
            game = False
    
   
    display.update()
    clock.tick(120)