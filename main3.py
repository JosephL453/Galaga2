import pgzrun
import random

WIDTH = 1200
HEIGHT = 600

bullet = Actor('bullet')
ship = Actor('galaga')
bug = Actor('bug')

enemies = []
bullets = []

ship.pos = (WIDTH/2, HEIGHT - 60)

speed = 5

for j in range(4):
    for i in range(8):
        enemies.append(Actor('bug'))

        enemies[-1].x = 100 + 50 * i
        enemies[-1].y = 80 + 50 * j
        direction = 1


score = 0
direction = 1
ship.dead = False
ship.countdown = 90


def display_score():
    screen.draw.text(str(score), (50,50), fontsize = 40)

def game_over():
    screen.draw.text("GAMEOVER", (WIDTH/2, HEIGHT/2))


def on_key_down(key):
    if (not ship.dead and key == keys.SPACE):
        bullets.append(Actor('bullet'))
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y - 50


def update():
    global score, direction
    move_down = False
    

    if keyboard.left:
        if ship.dead == False:
            ship.x -= 5
            if ship.x <= 0:
                ship.x = 0
    if keyboard.right:
        if ship.dead == False:
            ship.x += 5
            if ship.x >= WIDTH:
                ship.x = WIDTH

    for i in bullets:
        if i.y <= 0:
            bullets.remove(i)
        else: 
            i.y -= 10
    if len(enemies) == 0:
        game_over()
    if len(enemies) > 0 and (enemies[-1].x > WIDTH -80 or enemies[0].x < 80):
        move_down = True
        direction *= -1
    
    for i in enemies:
        i.x += 5 * direction
        if move_down == True:
            i.y += 100
        if i.y > HEIGHT:
            enemies.remove(i)
        
        for j in bullets:
            if i.colliderect(j):
                sounds.eep.play()
                score += 100
                bullets.remove(j)
                enemies.remove(i)
                if len(enemies) == 0:
                    game_over()
        if i.colliderect(ship):
            ship.dead = True
    if ship.dead:
        ship.countdown -= 1

    if ship.countdown == 0:
        ship.dead = False
        ship.countdown = 90
        
        





def draw():
    screen.clear()
    screen.fill((0,0,255))

    for i in bullets:
        i.draw()
    for i in enemies:
        i.draw()
    if not ship.dead:
        ship.draw
    display_score()
    if len(enemies) == 0:
        game_over()

    



pgzrun.go()