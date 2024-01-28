while True:
    enemy1 = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy1)
    if distance < 10:
        # Attack if they get too close to the peasant.
        hero.attack(enemy1)
        pass
    # Else, stay close to the peasant! Use else.
    else:
        hero.moveXY(40, 37)
