# Remember that enemies may not yet exist.
while True:
    enemy1 = hero.findNearestEnemy()
    if enemy1:
        # If there is an enemy, attack it!
        hero.attack(enemy1)
        pass
