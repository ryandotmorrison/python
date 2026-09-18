playing = True
score = 0
score_text = codesters.Text(f"Score:{score}", -210, 238)
dx = 1
dy = 0
grow = 5
apple_x = random.randint(-24, 24)
apple_y = random.randint(-24, 24)
a = codesters.Circle(apple_x * 10, apple_y * 10, 10, "red")
def chomp(head):
    global apple_x,apple_y,a,grow,score,score_text
    if head[0] == apple_x and head[1] == apple_y:
        grow = 1
        score += 1
        score_text.set_text(f"Score:{score}") 
        stage.remove_sprite(a)
        apple_x = random.randint(-24, 24)
        apple_y = random.randint(-24, 24)
        a = codesters.Circle(apple_x * 10, apple_y * 10, 10, "red")

def crash(head):
    global dx,dy,playing
    if head[0] > 24 or head[0] < -24 or head[1] > 24 or head[1] < -24:
        playing = False
    for counter in snake_xy:
        if head is not counter and head[0] == counter[0] and head[1] == counter[1]:
            playing = False
snake_xy = []
def left_key():
    global dx,dy
    dx = -1
    dy = 0
stage.event_key("left", left_key)

def right_key():
    global dx,dy
    dx = 1
    dy = 0
stage.event_key("right", right_key)

def up_key():
    global dx,dy
    dx = 0
    dy = 1
stage.event_key("up", up_key)

def down_key():
    global dx,dy
    dx = 0
    dy = -1
stage.event_key("down", down_key)

def main():
    global dx,dy,snake_xy,grow,playing
    snake_xy.append((0,0))
    snakey = []
    c = codesters.Circle(snake_xy[0][0], snake_xy[0][1], 10, "blue")
    snakey.append(c)
    while playing:
        head = snake_xy[len(snake_xy)-1]
        snake_xy.append((head[0] + dx,head[1] + dy))
        head = snake_xy[len(snake_xy)-1]
        c = codesters.Circle(head[0]*10, head[1]*10, 10, "blue")
        snakey.append(c)
        chomp(head)
        crash(head)
        if grow == 0:
            snake_xy.pop(0)
            stage.remove_sprite(snakey[0])
            snakey.pop(0)
        else:
            grow -= 1
        stage.wait(0.1)

main()
