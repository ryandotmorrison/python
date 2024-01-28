# Use your cleverest programming tricks to outwit and overpower your opponent!
while True:
    enemy = hero.findNearestEnemy()
    if hero.isReady("bash"):
        hero.bash(enemy)
    else:
        hero.attack(enemy)
