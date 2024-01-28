# Stay in the middle and defend!

while True:
    enemy1 = hero.findNearestEnemy()
    if enemy1:
        # Either attack the enemy...
        hero.attack(enemy1)
        pass
    else:
        # ... or move back to your defensive position.
        hero.moveXY(40, 34)
        pass
