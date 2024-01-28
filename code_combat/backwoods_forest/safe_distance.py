# Collect coins to repair the cart while staying close to the peasant!

while True:
    item = hero.findNearestItem()
    # Change the if-statement to check if the distance from the hero to the
    #coin is less than 15.
    
    if item.type == "coin" and distance < 15:
        distance = hero.distanceTo(item)
    if item:
        hero.moveXY(item.pos.x,item.pos.y)
        # Move to the red X after collecting the coin.
        hero.moveXY(42, 45)
