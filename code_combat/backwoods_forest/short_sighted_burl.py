# Collect coins and run, or else the burl will find you.

# This function allows your hero take an item.# Write the function "checkTakeRun" with one parameter.
# If the item exists, use "takeItem" function to take it.
# Go back to the start (green mark), with or without the item.
def checkTakeRun(target):
    if target:
        hero.moveXY(target.pos.x, target.pos.y)
    hero.moveXY(40, 12)

# Don't change this code.
while True:
    hero.moveXY(16, 56)
    coin = hero.findNearestItem()
    checkTakeRun(coin)
    hero.moveXY(64, 56)
    coin = hero.findNearestItem()
    checkTakeRun(coin)
