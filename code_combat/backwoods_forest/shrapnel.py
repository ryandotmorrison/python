# Use charges to soften up packs of ogres.
# Then pick them off with your bow.

while True:
    enemy1 = hero.findNearestEnemy()
    if enemy1:
        if hero.isReady("throwAt"):
            distance = hero.distanceTo(enemy1)
            # Only throwAt if the ogres are more than 15m away.
            # Use "if" to compare distance to 15.
            if hero.distanceTo(enemy1)>15:
                hero.throwAt(enemy1)
                # Use "else" to attack if you're not throwing.
            else:
                hero.attack(enemy1)
