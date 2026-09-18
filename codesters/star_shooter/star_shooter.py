stage.set_background("space")
stage.disable_all_walls()
spaceship = "https://i.ibb.co/4N3tSDH/Bevouliin-dino-spaceship-flying-game-character.png"
star = codesters.Sprite(spaceship)
star.set_size(0.25)
star.go_to(-200, 0)
ship = "https://i.ibb.co/PTsxxr3/Bevouliin-smiling-spaceship-game-character.png"
fish = codesters.Sprite(ship)
star.lives = 20
fish.lives = 20
startext = codesters.Text("Lives: {}".format(star.lives), -100, 200, "red")
fishtext = codesters.Text("Lives: {}".format(fish.lives), 100, 200, "blue")
fish.set_size(0.25)
fish.go_to(200, 0)
fish.flip_right_left()
def up_key(sprite):
    sprite.move_up(20)
    
fish.event_key("w", up_key)
star.event_key("up", up_key)
def down_key(sprite):
    sprite.move_down(20)
    
star.event_key("down", down_key)
fish.event_key("s", down_key)

def space_bar(sprite):
    # sprite = codesters.Triangle(x, y, size, "color")
    laser = codesters.Triangle(star.get_x(), star.get_y(), 15, "#A2FF00")
    laser.turn_right(90)
    laser.set_x_speed(5)


    
star.event_key("space", space_bar)               

def shoot(sprite):
    # sprite = codesters.Triangle(x, y, size, "color")
    laser = codesters.Triangle(fish.get_x(), fish.get_y(), 15, "#00FFF0")
    laser.turn_left(90)
    laser.set_x_speed(-5)


    
fish.event_key("e", shoot)

def collision(sprite, hit_sprite):
    my_var = hit_sprite.get_color() 
    if my_var == "#00FFF0":
        star.lives -= 1
        startext.set_text("Lives: {}".format(star.lives))
        stage.remove_sprite(hit_sprite)
        if star.lives < 1:
            stage.remove_sprite(sprite)
star.event_collision(collision)

def collision2(sprite, hit_sprite):
    my_var = hit_sprite.get_color() 
    if my_var == "#A2FF00":
        fish.lives -= 1
        fishtext.set_text("Lives: {}".format(fish.lives))
        stage.remove_sprite(hit_sprite)
        if fish.lives < 1:
            stage.remove_sprite(sprite)
fish.event_collision(collision2)
