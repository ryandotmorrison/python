hero.moveDown()

# Mama always said to eat random mushrooms you find in dungeons.
hero.moveDown()
hero.moveRight()
hero.moveDown()
hero.moveUp()
hero.moveLeft()
hero.moveDown()
hero.moveDown()
hero.moveRight()
hero.moveRight()
hero.moveUp()
hero.moveUp()
hero.moveUp()
# Find your way to the Dungeon Keeper.
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
