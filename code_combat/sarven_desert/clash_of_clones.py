# You'll need good strategy to win this one!
# Your clone will have the same equipment you have!
# But, they're not very skilled at using special powers.
while True:
    enemy = hero.findNearestEnemy()
    if enemy.type != 'sand-yak':
        if hero.isReady("chain-lightning"):
            hero.cast("chain-lightning", enemy)
        # hero.cast("shockwave", enemy)
        # hero.cast("haste", self)
        # hero.cast("slow", enemy)
        # hero.attack(enemy)
    # if hero.health < 200:
    #     hero.moveXY(48, 67)
    #     break
    if enemy.type != 'sand-yak':
        if enemy.type == "archer":
            hero.attack(enemy)
        if hero.isReady("bash"):
            hero.bash(enemy)
        else:
            hero.attack(enemy)
