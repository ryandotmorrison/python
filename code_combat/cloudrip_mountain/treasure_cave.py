# That ogre was defeated instantly! Better just avoid that yeti.

# We've hacked your fire-traps to go off after 5 seconds.
# The clearing to the north would be a good place for an explosive distraction.
# The yeti won't stay distracted forever, so hurry and grab the coins!
# After that run to the camp!
# while True:

hero.moveXY(64, 44)
# hero.moveXY(44, 47)
# hero.buildXY("fire-trap", 39, 67)
# hero.buildXY("fire-trap", 44, 47)
hero.buildXY("fire-trap", 64, 44)
hero.moveXY(44, 8)
# hero.moveXY(23, 26)
while True:
    item = hero.findNearestItem()
    if item:
        hero.moveXY(item.pos.x, item.pos.y)
        # hero.moveXY(64, 16)
    else:
        hero.move({'x':64,'y':16})

