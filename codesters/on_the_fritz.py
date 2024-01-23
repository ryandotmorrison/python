stage.set_background("cyber_blue")
stage.disable_all_walls()
bot = codesters.Sprite("robot7")
bot.set_size(0.5)
bot.go_to(0, 150)
lives = 25
score = 0
# sprite = codesters.Text("text", x, y)
display_lives = codesters.Text("Lives: {} ".format(lives), -167, 187)

# sprite = codesters.Text("text", x, y)
display_score = codesters.Text("Score: {} ".format(score), 167, 187)

def right_key():
    bot.move_right(20)
stage.event_key("right", right_key)

def left_key():
    bot.move_left(20)
stage.event_key("left", left_key)

def maketreasurechest():
    goal = codesters.Sprite("treasurechest")
    goal.set_size(0.5)
    randomx = random.randint(-250, 249)
    goal.go_to(randomx, -250)
    goal.set_y_speed(5)

def makewaterbottle():
    waterbottle = codesters.Sprite("waterbottle")
    waterbottle.set_size(0.5)
    randomx = random.randint(-250, 249)
    waterbottle.go_to(randomx, -250)
    waterbottle.set_y_speed(5)

def collision(sprite, hit_sprite):
    global lives, score
    my_var = hit_sprite.get_image_name()
    if my_var is "waterbottle":
        lives -= 1
        display_lives.set_text("Lives: {}".format(lives))
        stage.remove_sprite(hit_sprite)
    elif my_var is "treasurechest":
        score += 1
        display_score.set_text("Score: {}".format(score))
        stage.remove_sprite(hit_sprite)
bot.event_collision(collision)

while lives > 0:
    makewaterbottle()
    maketreasurechest()
    stage.wait(1)



