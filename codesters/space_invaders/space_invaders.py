game_over = False
lives = 5
stage.set_background("space")
stage.disable_ceiling()
stage.disable_floor()
p = codesters.Sprite("rocket",1,-220)
aliens = []
# alien code
def createAliens():
    for y in range(5):
        for x in range(7):
            alien = codesters.Sprite("L2_invader_58b",-228 + x*50 ,230 - y*50)
            aliens.append(alien)
            alien.set_size(0.15)
createAliens()
p.set_size(0.3)
canShoot = True

def alienCollision(alien,hit_sprite):
    global game_over
    if hit_sprite.get_color() == "#C6A664":
        stage.remove_sprite(alien)
        aliens.remove(alien)
        stage.remove_sprite(hit_sprite)
        if len(aliens) == 0:
            game_over = True

# player code
def left_key():
    if p.get_left() > -240:
        p.move_left(20)
stage.event_key("left", left_key)

def right_key():
    if p.get_x() < 240:
        p.move_right(20)
stage.event_key("right", right_key)

def space_bar():
    global canShoot
    if canShoot == True and game_over == False:
        canShoot = False
        laser = codesters.Circle(p.get_x(), p.get_y(),  12.5, "#C6A664")
        laser.set_y_speed(5)
        stage.wait(0.25)
        canShoot = True
stage.event_key("space", space_bar)

def playerCollision(p,hit_sprite):
    global game_over,lives
    if hit_sprite.get_color() == "green":
        lives -= 1
        stage.remove_sprite(hit_sprite)
        if lives == 0:
            game_over = True 
            stage.remove_sprite(p)

p.event_collision(playerCollision)
# alien code again
def alienShoot(alien):
    ranFire = random.randint(1,8)
    if ranFire == 8:
        bullet = codesters.Ellipse(alien.get_x(), alien.get_y(), 5, 15, "green")
        bullet.set_y_speed(-5)

for alien in aliens:
    alien.event_collision(alienCollision)

def alienMove(steps):
    for i in range(10):
        if game_over == False:
            for alien in aliens:
                alien.move_right(steps)
                alienShoot(alien)
        else:
            break
    if game_over == False:
        for alien in aliens:
            alien.move_down(50)
            alienShoot(alien)

while game_over == False:
    alienMove(15)
    alienMove(-15)

if lives == 0:
    lose = codesters.Text("Lose.")
else:
    win = codesters.Text("Win.")
