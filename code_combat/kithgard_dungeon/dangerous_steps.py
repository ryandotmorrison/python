# Defeat the ogres using their names.
hero.moveRight(1)
# Defeat the first pair of ogres.
enemy1 = hero.findNearestEnemy()
hero.attack(enemy1)
enemy2 = hero.findNearestEnemy()
hero.attack(enemy2)
hero.moveRight(2)
# Defeat the second pair of ogres.
hero.attack("Kro")
hero.attack("Ergo")
