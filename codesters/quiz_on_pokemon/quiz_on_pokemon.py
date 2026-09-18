stage.set_background_color("blue")
q = []
a = []
ca = []
qNum = 0
c = 0
qText = codesters.Text("q", -28, 111, "red")
aText = codesters.Text("a", -146, -19, "red")
bText = codesters.Text("b", -146, -119, "red")
cText = codesters.Text("c", 116, -19, "red")
dText = codesters.Text("d", 116, -119, "red")
display = codesters.Text("", -21, 45, "red")
text = [aText,bText,cText,dText]

def createQ():
    # q1
    q.append("How many regions are in Pokémon?")
    a.append(["1","5","10","18"])
    ca.append(cText)
    # q2
    q.append("How many different Pokémon are there?")
    a.append(["500","750","1,025","1,000"])
    ca.append(cText)
    # q3
    q.append("Which Pokémon is #923?")
    a.append(["Pawmot","Pecharunt","Dachsbun","Terapagos"])
    ca.append(aText)
    # q4
    q.append("What type is Necrozma?")
    a.append(["Dark","Ghost","Dragon","Psychic"])
    ca.append(dText)
    # q5
    q.append("How many Ultra Beasts are there?")
    a.append(["13","11","12","10"])
    ca.append(bText)
createQ()

def showQ():
    global qNum
    qText.set_text(q[qNum])
    aText.set_text(a[qNum][0])
    bText.set_text(a[qNum][1])
    cText.set_text(a[qNum][2])
    dText.set_text(a[qNum][3])
showQ()

def nextQ():
    global qNum,c
    qNum += 1
    if qNum < len(q):
        showQ()
    else:
        qText.hide()
        aText.hide()
        bText.hide()
        cText.hide()
        dText.hide()
        display.set_text(f"You got {c} out of 5")


def click(choice):
    global c
    if choice == ca[qNum]:
        display.set_text("Correct!")
        c += 1
    else:
        display.set_text("Wrong!")
    stage.wait(1)
    display.set_text("")
    nextQ()
for t in text:
    t.event_click(click)
