stage.set_background("cyber_blue")
player = codesters.Rectangle(-22, -212, 125, 15, "red")
brick_list = []

def build_bricks():
    for y in range(5):
        for x in range(9):
            brick = codesters.Rectangle(-222 + 55*x, 223-30*y, 50, 25, "green")
            brick_list.append(brick)

def left_key():
    player.move_left(40)
stage.event_key("left", left_key)

def right_key():
    player.move_right(40)
stage.event_key("right", right_key)

b = codesters.Circle(0, 0, 20, "blue")
y_speed = random.randint(5,10)
x_speed = random .randint(-5,5)
b.set_x_speed(x_speed)
b.set_y_speed(y_speed)

def collision(sprite, hit_sprite):
    if hit_sprite == player:
        b.set_y_speed(b.get_y_speed()*-1)
        if b.get_x() > player.get_left() and b.get_x() < player.get_x():
            b.set_x_speed(random.randint(-5,-1))
        elif b.get_x() < player.get_right() and b.get_x() > player.get_x():
            b.set_x_speed(random.randint(1,5))
    if hit_sprite in brick_list:
        b.set_y_speed(b.get_y_speed()*-1)
        stage.remove_sprite(hit_sprite)
b.event_collision(collision)

def floor_collision():
    if b.get_y() < -230:
        return False
    else:
        return True

def main():
    build_bricks()
    while len(brick_list) > 0:
        if not floor_collision():
            break
        stage.wait(0.01)
    b.set_x_speed(0)
    b.set_y_speed(0)

if __name__ == "__main__":
    main()
