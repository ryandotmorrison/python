bob = codesters.Sprite("Bob_b17", -10, -198)
stage.disable_floor()
stage.disable_ceiling()
stage.set_background("winter")
bob.set_size(0.3)
bob.chuck_snow = False
bob.chuck_ice = False

def left_key():
    bob.move_left(20)
stage.event_key("left", left_key)

def right_key():
    bob.move_right(20)
stage.event_key("right", right_key)

def down_key():
    bob.move_down(20)
stage.event_key("down", down_key)

def up_key():
    bob.move_up(20)
stage.event_key("up", up_key)

def space_bar():
    if bob.chuck_snow == False:
        bob.chuck_snow = True
        snowball = codesters.Sprite("snowball_223", bob.get_x(), bob.get_y())
        snowball.set_y_speed(18)
        snowball.set_size(0.1)
        stage.wait(0.1)
        bob.chuck_snow = False
stage.event_key("space", space_bar)

def f_key():
    if bob.chuck_ice == False:
        bob.chuck_ice = True
        ice = codesters.Sprite("freeze_b3d", bob.get_x(), bob.get_y())
        ice.set_y_speed(9)
        ice.set_size(0.2)
        stage.wait(0.2)
        bob.chuck_ice = False
stage.event_key("f", f_key)



