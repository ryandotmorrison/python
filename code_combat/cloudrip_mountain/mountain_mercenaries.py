# Gather coins to summon soldiers and have them attack the enemy.
while True:
    item = hero.findNearestItem()
    if (item):
        hero.move(item.pos)
    if hero.gold > hero.costOf("soldier"):
        hero.summon("soldier")
    enemy = hero.findNearestEnemy()
    if enemy:
        soldiers = hero.findFriends()
        soldierIndex = 0
        while (soldierIndex < len(soldiers)):
            soldier = soldiers[soldierIndex]
            hero.command(soldier, "attack", enemy)
            soldierIndex += 1
