# Ask the healer for help when you're under one-half health.

while True:
    enemy = hero.findNearestEnemy()
    currentHealth = hero.health
    healingThreshold = hero.maxHealth / 2
    # If your current health is less than the threshold,
    # move to the healing point and say, "heal me".
    # Otherwise, attack. You'll need to fight hard!
    if enemy:
        if enemy:
            hero.attack(enemy)
        if hero.health < healingThreshold / 2:
            hero.moveXY(65, 46)
            hero.say("heal me")
        else:
            affected = hero.hasEffect("shrink")
    else:
        affected = hero.hasEffect("shrink")
