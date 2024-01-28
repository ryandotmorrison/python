# We are field testing a new battle unit: the decoy.
# Build 4 decoys, then report the total to Naria.

decoysBuilt = 0
while True:
    coin = hero.findNearestItem()
    
    if coin:
        # Collect the coin!
        hero.moveXY(coin.pos.x, coin.pos.y)
        pass
    # Each decoy costs 25 gold.
    # If hero.gold is greater than or equal to 25:
    if hero.gold >= 25:
        
        # buildXY a "decoy"
        hero.buildXY("decoy", 36, 30)
        # Add 1 to the decoysBuilt count.
        decoysBuilt += 1
    if decoysBuilt == 4:
        # Break out of the loop when you have built 4.
        break
        pass
    
hero.say("Done building decoys!")
hero.moveXY(14, 36)
# Say how many decoys you built.
hero.say(decoysBuilt)
