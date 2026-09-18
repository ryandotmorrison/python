import turtle
import random
turtle.setup(1000, 1000)
turtle.screensize(2500, 2500)

ryan = turtle.Turtle()
#() is necessary to know it is not an int object and is a turtle object

ryan.speed(10)
ryan.shape("turtle")
ryan.pensize(6)
ryan.pencolor("black")
turtle.bgcolor("gold")
ryan.fillcolor("blue")

def polygon(sides):
    for i in range(sides):
        ryan.forward(50)
        ryan.right(360/sides)

def pen_goto(a, b):
    ryan.penup()
    ryan.goto(a,b)
    ryan.pendown()

width = 1200
height = 600


def coordinate_axis():
    pen_goto(-width/2, 0)
    ryan.forward(width)

    pen_goto(0, -height/2)
    ryan.left(90)   #90 degree turn
    ryan.forward(height)
    
polygon(30)
pen_goto(250, 250)
polygon(20)

turtle.setup(width, height)
coordinate_axis()

colors = ["red","yellow","blue","green","purple","orange","black","gold","silver"]
def draw_unique_figure():
    ryan.pendown()
    for i in range(100):
        a = random.randint(-300, 300)
        b = random.randint(-300, 300)
        ryan.pencolor(colors[i % 7])
        pen_goto(a, b)
        ryan.home()

#draw_unique_figure()
def pen_home():
    ryan.penup()
    ryan.home()
    ryan.down()
    
def draw_unique_figure2():
    for i in range(100):
        ryan.pensize(random.randint(1, 6))
        ryan.pencolor(colors[i % 7])
        ryan.setheading(random.randint(0,359))
        ryan.forward(random.randint(0,300))
        pen_home()

def spiral():
    ryan.pencolor("black")
    ryan.pensize(4)
    for i in range(240):
        ryan.forward(2+ i/4)
        ryan.right(30- i/12)

draw_unique_figure2()
spiral()

ryan.hideturtle()


turtle.end_fill()
turtle.done()
