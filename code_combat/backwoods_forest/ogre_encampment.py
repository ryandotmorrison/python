# If there is an enemy, attack it.
# Otherwise, attack the chest!

while True:
    # Use if/else.
    if enemy1:
        enemy1 = hero.findNearestEnemy()
        hero.attack(enemy1)
    else:
        hero.attack("Chest")
