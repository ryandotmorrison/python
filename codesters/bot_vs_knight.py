stage.set_background("castle")
knight = codesters.Sprite("knight2")
knight.go_to(-200, -40)
robot7 = codesters.Sprite("robot7")
robot7.set_size(0.6)
robot7.go_to(200, -40)

def right_key():
    knight.move_right(10)
stage.event_key("right", right_key)

def left_key():
    knight.move_left(10)
stage.event_key("left", left_key)

def up_key():
    knight.move_up(10)
stage.event_key("up", up_key)

def down_key():
    knight.move_down(5)
stage.event_key("down", down_key)

def a_key():
    robot7.move_left(10)
stage.event_key("a", a_key)

def d_key():
    robot7.move_right(10)
stage.event_key("d", d_key)

def w_key():
    robot7.move_up(10)
stage.event_key("w", w_key)

def s_key():
    robot7.move_down(5)
stage.event_key("s", s_key)
def collision(sprite, hit_sprite):
    if hit_sprite.get_color() is "blue":
        stage.remove_sprite(hit_sprite)
        knight.say("OW!",1)
    else:
        knight.move_left(200)

knight.event_collision(collision)
def space_bar():
    #sprite = codesters.Arrow(x-start, y-start, x-end, y-end, double_headed)
    laser = codesters.Arrow(robot7.get_x(), robot7.get_y(), robot7.get_x()-50, robot7.get_y(), False)
    laser.set_color("blue")
    laser.set_x_speed(-80)
stage.event_key("space", space_bar)



