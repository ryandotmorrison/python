import turtle

name = "Ryan"
name2 = 'Elvin'

print(name2 + " is silly.")
print(name + " is smart.")

print(name, "Type:", type(name))
#print out the variable type of a variable

c = "1234"
newc = int(c)
#changwa the variable type of string to an integer
print(newc)

print(6 > 4)
#this is a boolean variable, it's values are either True, False, 0 or 1

print(1 + 2 == 2)
#== comparison, it it is equal, single equals is assignment

print(True and False)

print(not False)
print(not True)

list3 = ["Austin","Tony","Luke","William","Oliver"]
#           0        1       2       3         4
#every list starts from 0, not from 1!
print(list3[1:])
print(list3[-1])
print(list3[1:3])
print(list3[0:5])

#list operations are appending,modifying or itereating over items in a list
list3.append("Ryan")
list3.append("Albert")
print(list3)
list3.insert(1, "Derek")
print(list3)

list4 = ["Zack", "Max", "Mateo"]
list3.extend(list4)
print(list3)

list3.pop()
#pop will remove the last element from the list
print(list3)
list3.remove("Zack")
print(list3)

ryan = turtle.Turtle()
ryan.shape("turtle")
ryan.speed(5)

if ((5 > 4) == True):
    ryan.forward(200)
    ryan.right(90)

ryan.speed(40)

colors = ["red","yellow","green","purple","brown","blue"]
colors.insert(1, "orange")
colors.insert(3, "cyan")
print(colors)

for i in range(360):
    #the % is modulus command, find remainder from division, allow us to pick random color
    ryan.pencolor(colors[i % 8])
    ryan.pensize(1 + i / 100)
    ryan.forward(i)
    ryan.left(59)

x_width = 1200
y_height = 800
turtle.setup(x_width, y_height)
turtle.bgcolor("black")

colors.append("#1E90FF")
colors.append("#FF4500")

for color in colors:
    ryan.pencolor(color)
    ryan.forward(20)
    ryan.left(10)

for i in range(720):
    ryan.pencolor(colors[i % 10])
    ryan.pensize(1 + i / 10)
    ryan.forward(i)
    ryan.left(59)

