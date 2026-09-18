# Use while loops to pick out the ogre

while True:
    enemies = hero.findEnemies()
    for enemy in enemies:
        if enemy.type != "sand-yak":
            while enemy.health > 0:
                hero.attack(enemy)    
    
# Between waves, move back to the center.
hero.moveXY(40, 32) 
