# Move to 'Eszter' and get the secret number from her.
hero.moveXY(16, 32)
esz = hero.findNearestFriend().getSecret()

# Multiply by 3 and subtract 2 to get 'Tamas's number.
# Remember to use parentheses to do calculations in the right order.
# Move to 'Tamas' and say his magic number.
tam = (esz * 3) - 2
hero.moveXY(24, 28)
hero.say(tam)

# Subtract 1 and multiply by 4 to get 'Zsofi's number.
# Move to 'Zsofi' and say her magic number.
zso = (tam - 1) * 4
hero.moveXY(32, 24)
hero.say(zso)
# Add 'Tamas's and 'Zsofi's numbers, then divide by 2 to get 'Istvan's number.
# Move to 'Istvan' and say his magic number.
ist = (tam + zso)
hero.moveXY(40, 20)
hero.say(ist)
# Add 'Tamas's and 'Zsofi's numbers. Subtract 'Istvan's number from 'Zsofi's. Multiply the two results to get 'Csilla's number.
# Move to 'Csilla' and say her magic number.
