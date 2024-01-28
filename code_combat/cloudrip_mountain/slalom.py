# Use object literals to walk the safe path and collect the gems.
# You cannot use moveXY() on this level! Use move() to get around.
gems = hero.findItems()

while hero.pos.x < 20:
	# move() takes objects with x and y properties, not just numbers.
	hero.move({'x': 20, 'y': 35})

while hero.pos.x < 25:
	# A gem's position is an object with x and y properties.
	gem0 = gems[0]
	hero.move(gem0.pos)

# While your x is less than 30,
# Use an object to move to 30, 35.
while hero.pos.x < 30:
    hero.move({ "x": 30, "y": 35 })
# While your x is less than 35,
# Move to the position of gems[1].
while hero.pos.x < 35:
    gem1 = gems[1]
    hero.move(gem1.pos)
# Get to the last couple of gems yourself!
while hero.pos.x < 40:
    hero.move({ "x": 40, "y": 35 })

while hero.pos.x < 45:
    gem2 = gems[2]
    hero.move(gem2.pos)

while hero.pos.x < 50:
    hero.move({ "x": 50, "y": 35 })

while hero.pos.x < 55:
    gem3 = gems[3]
    hero.move(gem3.pos)
