letter_list = []
game_over = False
turn = 1
board = []
def make_board():
    for y in range(3):
        for x in range(3):
            box = codesters.Square(-128 + 100*x, 95 - 100*y, 75, "#5E2129")
            board.append(box)
            letter_list.append(0)

make_board()

def click(sprite):
    global turn,game_over
    box_index = board.index(sprite)
    if letter_list[box_index] == 0 and game_over == False:
        if turn == 1:
            x = codesters.Text("X", sprite.get_x(), sprite.get_y(), "white")
            x.set_text_size(50)
            letter_list[box_index] = 1
            check_winner()
            turn = 2
        else:
            o = codesters.Text("O", sprite.get_x(), sprite.get_y(), "white")
            o.set_text_size(50)
            letter_list[box_index] = 2
            check_winner()
            turn = 1
for box in board:
    box.event_click(click)

def check_boxes(b1,b2,b3):
    global turn,game_over
    if letter_list[b1] == turn and letter_list[b2] == turn and letter_list[b3] == turn:
        if turn == 1:
            w = codesters.Text("X WINS!", 100, 200)
        else:
            w = codesters.Text("O WINS!", 100, 200)
        game_over = True

def check_winner():
    global turn
    check_boxes(0,1,2)
    check_boxes(3,4,5)
    check_boxes(6,7,8)
    check_boxes(0,4,8)
    check_boxes(6,4,2)
    check_boxes(0,3,6)
    check_boxes(2,5,8)
    check_boxes(1,4,7)
