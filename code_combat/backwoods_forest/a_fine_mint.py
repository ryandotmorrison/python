# Peons are trying to steal your coins!
# Write a function to squash them before they can take your coins.

def pickUpCoin():
    coin = hero.findNearestItem()
    if coin:
        hero.moveXY(coin.pos.x, coin.pos.y)

# Write the attackEnemy function below.
# Find the nearest enemy and attack them if they exist!
def attackEnemy():
    enemy1 = hero.findNearestEnemy()
    if enemy1:
        hero.attack(enemy1)

while True:
    attackEnemy() # ∆ Uncomment this line after you write an attackEnemy function.
    pickUpCoin()
