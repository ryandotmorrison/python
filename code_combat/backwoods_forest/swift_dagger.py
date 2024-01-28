# Use your bow at long range and dagger at short range.

while True:
    enemy1 = hero.findNearestEnemy()
    if enemy1:
        distance = hero.distanceTo(enemy1)
        if distance < hero.throwRange:
            # Throw your dagger at the enemy if "throwAt" is ready.
            if hero.isReady("throwAt"):
                hero.throwAt(enemy1)
            else:
            # Attack the enemy with your bow.
                hero.attack(enemy1)
