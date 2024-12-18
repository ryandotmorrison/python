stage.set_background("underwater")
stage.disable_ceiling()
r = codesters.Sprite("robot2")
r.location = ""
jumping = False
platforms = []
coins = []
b = codesters.Rectangle(159, -201, 100, 50, "#2A6478")
b.set_gravity_off()


r.set_size(0.3)
stage.set_gravity(10)

def createPlats():
    for i in range(3):
        plat = codesters.Rectangle(-125, 150 - 125*i, 120, 20, "#7E2B9D")
        platforms.append(plat)
    wall = codesters.Rectangle(120, -75, 50, 300, "#7E2B9D")
    platforms.append(wall)
createPlats()

def addCollectables():
    c = codesters.Circle(117, 85, 15, "#CDA434")
    coins.append(c)
    c = codesters.Circle(-138, -72, 15, "#CDA434")
    coins.append(c)
    c = codesters.Circle(-144, 46, 15, "#CDA434")
    coins.append(c)
    c = codesters.Circle(-130, 175, 15, "#CDA434")
    coins.append(c)
    c = codesters.Circle(225, -198, 15, "#CDA434")
    coins.append(c)
addCollectables()
def right_key():
    r.set_x_speed(5)
stage.event_key("right", right_key)

def left_key():
    r.set_x_speed(-5)
stage.event_key("left", left_key)

def space_bar():
    global jumping
    if jumping == False:
        jumping = True
        r.jump(20)
        r.set_gravity_on()
stage.event_key("up", space_bar)

def lvl1():
    g = codesters.Rectangle(0, -240, 500, 50, "#7E2B9D")
    platforms.append(g)
lvl1()
for plat in platforms:
    plat.set_gravity_off()
    

for c in coins:
    c.set_gravity_off()
    
def collision(sprite, hit_sprite):
    global jumping
    if hit_sprite in platforms:
        if sprite.get_y() > hit_sprite.get_top():
            #landing
            r.location = hit_sprite
            r.set_bottom(hit_sprite.get_top())
            r.set_y_speed(0)
            r.set_gravity_off()
            jumping = False
        if sprite.get_y() < hit_sprite.get_bottom():
            r.set_y_speed(0)
            r.set_top(hit_sprite.get_bottom())
        if sprite.get_x() < hit_sprite.get_left():
            r.set_x_speed(r.get_x_speed()*-1)
            r.set_right(hit_sprite.get_left())
        if sprite.get_x() > hit_sprite.get_right():
            r.set_x_speed(r.get_x_speed()*-1)
            r.set_left(hit_sprite.get_right())
    if hit_sprite is b:
        r.jump(22)
    if hit_sprite in coins:
        stage.remove_sprite(hit_sprite)
        coins.remove(hit_sprite)
        if len(coins) == 0:
            stage.remove_sprite(r)
            sprite = codesters.Text("You Win!", -1, 49, "#CDA434")
            sprite.set_text_size(100)


r.event_collision(collision)

def interval():
    r.set_x_speed(r.get_x_speed()*0.7)
    if r.location is not "":
        fall_width = (r.get_width()+ r.location.get_width())/2
        if abs(r.get_x() - r.location.get_x()) > fall_width:
            r.set_gravity_on()

stage.event_interval(interval, 0.05)



