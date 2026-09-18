letters_guessed = []
word_display = []
stage.set_background("cyber_blue")
gg = codesters.Sprite("wizard")
gg.go_to(-11, -225)
t = turtle.Turtle()
t.shape("turtle")
t.speed(2.5)
def drawhangman():
    if no_guesses == 5:
        # draw post
        t.penup()
        t.setposition(154, -142)
        t.pendown()
        t.left(90)
        t.forward(300)
        t.left(90)
        t.forward(125)
        t.left(90)
        t.forward(25)
        # draw head
        t.penup()
        t.goto(-20, 83)
        t.pendown()
        t.circle(50)
    elif no_guesses == 4:
        # draw body
        t.penup()
        t.goto(26, 33)
        t.pendown()
        t.forward(95)
    elif no_guesses == 3:
        # draw left leg
        t.right(45)
        t.forward(75)
        t.penup()
        t.back(75)
    elif no_guesses == 2:
        # draw right leg
        t.left(90)
        t.pendown()
        t.forward(75)
    elif no_guesses == 1:
        # draw right arm
        t.penup()
        t.goto(26, 7)
        t.pendown()
        t.forward(75)
    elif no_guesses == 0:
        # draw left arm
        t.penup()
        t.goto(26, 7)
        t.right(90)
        t.pendown()
        t.forward(75)
random_words = ["station","cooperative","holiday","fibre","weakness"]
good_guesses = []
gg.set_size(0.5)
no_guesses = 6
word = random.choice(random_words)
for good in range(len(word)):
    good_guesses.append("_")
    word_display.append(codesters.Text("_",-220 + 15 * good,203))
def update_display():
    for i in range(len(word_display)):
        word_display[i].set_text(good_guesses[i])
def checkword():
    return "_" not in good_guesses
while no_guesses > 0 and not checkword():
    choice = gg.ask("Guess a letter.")
    if len(choice) > 1:
        gg.say("No guessing more than 2 letters.",2)
        continue
    elif choice in letters_guessed:
        gg.say("You already guessed that letter.",2)
        continue
    else:
        letters_guessed.append(choice)
        if choice in word:
            gg.say("Sí",1)
            for i in range(len(word)):
                if choice == word[i]:
                    good_guesses[i] = word[i]
                    print(good_guesses)
            update_display()
        else:
            gg.say("noooooooooooooooo!",1)
            no_guesses -=1
            drawhangman()



