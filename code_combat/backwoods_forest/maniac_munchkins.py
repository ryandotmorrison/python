# Another chest in the field for the hero to break open!
# Attack the chest to break it open.
# Some munchkins won't stand idly by while you attack it!
# Defend yourself when a munchkin gets too close.

while True:
    enemy1 = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy1)
    if hero.isReady("cleave"):
        # First priority is to cleave if it's ready:
        if hero.isReady("cleave"):
            hero.cleave(enemy1)
        pass
    elif distance < 5:
        # Attack the nearest munchkin that gets too close:
        hero.attack(enemy1)
        pass
    else:
        # Otherwise, try to break open the chest:
        # Use the name of the chest to attack: "Chest".
        hero.attack("Chest")
        pass
