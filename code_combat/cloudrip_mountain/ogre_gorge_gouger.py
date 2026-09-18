# You only have 20 seconds until the ogre horde arrives!
# Grab as much gold as you can, then retreat to your base and wall it off!
while hero.time < 20:
    # Collect coins
    hero.say("I should pick up a coin")
    
    
while hero.pos.x > 16:
    # Retreat behind the fence
    hero.say("I should retreat")
    hero.moveXY(11, 37)
    hero.buildXY("fence", 21, 38)
# Build a fence to keep the ogres out.
