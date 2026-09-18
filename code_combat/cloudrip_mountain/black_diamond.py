# prev = (0, 0)
while True:
    gem = hero.findNearest(hero.findItems())
    if gem:
        clear = hero.isPathClear(hero.pos, gem.pos)
        # The isPathClear method tells you if there’s an obstacle in the way.
        # If it’s clear, move() to gem.pos.
        if clear:
            # lastpos = {'x': hero.pos.x, 'y': hero.pos.y}
            hero.moveXY(gem.pos.x, gem.pos.y)
        else:
            # hero.moveXY(lastpos.x, lastpos.y)
            hero.move({'x':40,'y':35})
            # hero.moveXY(40, 35)
