# Destroy the mines!
# Use `say` to call out the range to the mines.
# Use division to calculate the range.

enemy1 = hero.findNearestEnemy()
distanceToEnemy = hero.distanceTo(enemy1)
# Say the result of the operation: distanceToEnemy divided by 3
hero.say(distanceToEnemy / 3)
hero.say("Fire!")
# Say second range: distanceToEnemy divided by 1.5
enemy2 = hero.findNearestEnemy()
distanceToEnemy = hero.distanceTo(enemy2)
hero.say(distanceToEnemy/1.5)
hero.say("Fire!")

# Say these things for motivation. Really. Trust us.
hero.say("Woo hoo!")
hero.say("Here we go!")
hero.say("Charge!!")

# Now, use a while-true loop to attack the enemies
while True:
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)
