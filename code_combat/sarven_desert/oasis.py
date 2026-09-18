# Move right to reach the oasis,
# Move left to avoid nearby yaks.
while True:
    x = hero.pos.x
    y = hero.pos.y
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) < 10:
        # Subtract 10 from x to move left.
        hero.moveXY(x-10, y)
        # Use moveXY to move to the new x, y position.
        hero.moveXY(x-10, y)
        pass
    else:
        # Add 10 to x to move right.
        hero.moveXY(x+10, y)
        # Use moveXY to move to the new x, y position.
        hero.moveXY(x+10, y)
        pass
