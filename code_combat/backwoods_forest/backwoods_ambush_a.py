# In this level you will use functions with two parameters.
# Look at the structure below, notice how there are two arguments.
# These are both accessible within the function. 
def checkAndAttack(x, y):
    # First move to the coordinates provided by the parameters.
    while True:
        
        enemy1 = hero.findNearestEnemy()
        hero.moveXY(24, 42)
        # Then check for an enemy.
    if enemy1:
        
        # If there is one, attack it!
        hero.attack(enemy1)
    pass

checkAndAttack(24, 42)
checkAndAttack(27, 60)
# Navigate to the last 3 x-marks and defeat any remaining munchkins.
hero.moveXY(42, 50)
if enemy1:
    hero.attack(enemy1)
pass
hero.moveXY(39, 24)
if enemy1:
    hero.attack(enemy1)
pass
hero.moveXY(55, 29)
if enemy1:
    hero.attack(enemy1)
pass
