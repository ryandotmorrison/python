# Defeat as many ogres as you can.
# Use 'cast' and 'canCast' for spells.
while True:
    enemy1 = hero.findNearestEnemy()
    if enemy1:
        if hero.canCast("chain-lightning"):
            hero.cast("chain-lightning", enemy1)
        else:
            hero.cast("lightning-bolt", enemy1)
