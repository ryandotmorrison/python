cards = []
face_1 = ""
face_2 = ""
turn = 1
def create_cards():
    for y in range(4):
        for x in range(4):
            card = codesters.Rectangle(-201+134*x, 190-125*y, 75, 105, "blue")
            card.id = x+(y*4)
            cards.append(card)

create_cards()

sprites = []

def deck():
    for i in range(2):
        sprites.append("Bounceman_c67")
        sprites.append("zoro_df1")
        sprites.append("nami_54f")
        sprites.append("Usopp_8f6")
        sprites.append("sanji_59d")
        sprites.append("chopper_92a")
        sprites.append("robin_c38")
        sprites.append("franky_c88")

deck()

def click(sprite):
    global turn,face_1,face_2
    if turn == 1:
        face_1 = codesters.Sprite(sprites[sprite.id], sprite.get_x(), sprite.get_y())
        face_1.set_size(0.4)
        turn = 2
    elif turn == 2:
        face_2 = codesters.Sprite(sprites[sprite.id], sprite.get_x(), sprite.get_y())
        face_2.set_size(0.4)
        stage.wait(1)
        
        if face_1.get_image_name() != face_2.get_image_name():
            stage.remove_sprite(face_1)
            stage.remove_sprite(face_2)
        turn = 1

for card in cards:
    card.event_click(click)

def shuffle():
    for i in range(len(sprites)-1):
        temp = sprites[i]
        bajrang_gun = random.randint(i+1, len(sprites)-1)
        sprites[i] = sprites[bajrang_gun]
        sprites[bajrang_gun] = temp

shuffle()
