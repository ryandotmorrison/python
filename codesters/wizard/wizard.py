stage.set_background("castle")
ew = codesters.Sprite("evilwizard",-180,125)
ew.hp = 10
ewit = codesters.Sprite("evilwitch",-180,-87)
ewit.hp = 10
w = codesters.Sprite("wizard",178,10)
w.hp = 5
w.set_size(0.9)

cast = False
evil = [ew,ewit]

def w_hit(sprite,hit_sprite):
    if hit_sprite in evil:
        stage.remove_sprite(sprite)
        hit_sprite.hp -= 1
        if hit_sprite.hp < 1:
            stage.remove_sprite(hit_sprite)
        hit_sprite.say("Owie",1)


def space_bar():
    global cast
    if cast == False and w.hp > 0:
        cast = True
        e = codesters.Sprite("electro_2cb",w.get_x(),w.get_y())
        e.event_collision(w_hit)
        e.set_size(0.5)
        e.set_rotation(random.randint(135,225))
        e.move_forward(500)
        stage.wait(0.5)
        cast = False
stage.event_key("space", space_bar)


def shield():
    global cast
    if cast == False and w.hp > 0:
        cast = True
        s = codesters.Sprite("shield_4be",80, 0)
        s.set_size(0.8)
        stage.wait(4)
        stage.remove_sprite(s)
        cast = False
stage.event_key("f", shield)

def ice():
    if ewit.hp > 0:
        i = codesters.Sprite("ice_0d1",ewit.get_x(),ewit.get_y())
        i.event_collision(e_ew_hit)
        i.set_size(0.5)
        i.set_rotation(random.randint(-45,45))
        i.move_forward(1000)

def doom():
    if ew.hp > 0:
        d = codesters.Sprite("doom_c78",ew.get_x(),ew.get_y())
        d.event_collision(e_ew_hit)
        d.set_size(0.5)
        d.set_rotation(random.randint(-45,45))
        d.move_forward(1000)

def e_ew_hit(sprite,hit_sprite):
    if hit_sprite == w:
        w.hp -= 1
        stage.remove_sprite(sprite)
        if w.hp <= 0:
            stage.remove_sprite(hit_sprite)
    if hit_sprite.get_image_name() == "shield_4be":
        stage.remove_sprite(sprite)

def interval():
    doom()
    ice()
stage.event_interval(interval, 2)
