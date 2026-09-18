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


def right_key():
    player.move_right(40)


b = codesters.Circle(0, 0, 20, "blue")
y_speed = random.randint(5,10)
x_speed = random.randint(-5,5)
b.set_x_speed(x_speed)
b.set_y_speed(y_speed)

def brick_collision():
    for brick in brick_list:
        if b.get_x() > brick.get_left() and b.get_x() < brick.get_right():
            if b.get_top() > brick.get_bottom() and b.get_top() < brick.get_y():
                b.set_top(brick.get_bottom())
                b.set_y_speed(b.get_y_speed()*-1)
                stage.remove_sprite(brick)
                brick_list.remove(brick)

def player_collision():
    if b.get_x() > player.get_left() and b.get_x() < player.get_right():
        if b.get_bottom() > player.get_bottom() and b.get_bottom() < player.get_top():
            b.set_bottom(player.get_top())
            b.set_y_speed(b.get_y_speed()*-1)
            if b.get_x() < player.get_x():
                b.set_x_speed(random.randint(-5,-3))
            elif b.get_x() > player.get_x():
                b.set_x_speed(random.randint(3,5))

def floor_collision():
    if b.get_y() < -230:
        return False
    else:
        return True

def main():
    build_bricks()
    while len(brick_list) > 0:
        stage.event_key("right", right_key)
        stage.event_key("left", left_key)
        brick_collision()
        player_collision()
        if not floor_collision():
            break
        stage.wait(0.0001)
    b.set_x_speed(0)
    b.set_y_speed(0)

if __name__ == "__main__":
    main()
