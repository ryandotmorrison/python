# Collect 25 gold, and then tell Naria the total.
# Use break to stop collecting when totalGold >= 25.

totalGold = 0
while True:
    coin = hero.findNearestItem()
    if coin:
        # Pick up the coin.
        hero.moveXY(coin.pos.x, coin.pos.y)
        # Add the coin's value to totalGold.
        # Get its value with:  coin.value
        totalGold = coin.value + totalGold
        pass
    if totalGold >= 25:
        # This breaks out of the loop to run code at the bottom.
        # The loop ends, code after the loop will run.
        break

# Done collecting gold!
hero.moveXY(58, 33)
# Go to Naria and say how much gold you collected.
hero.moveXY(58, 33)
hero.say(totalGold)
