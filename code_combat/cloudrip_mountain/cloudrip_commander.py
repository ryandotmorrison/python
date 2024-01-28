# Summon some soldiers, then direct them to your base.
friend = hero.findFriends()
# Each soldier costs 20 gold.
while hero.gold > hero.costOf("soldier"):
    hero.summon("soldier")
    
soldiers = hero.findFriends()
soldierIndex = 0
# Add a while loop to command all the soldiers.
# while soldierIndex <= len(soldiers):
while soldierIndex < len(soldiers):
# while soldierIndex <= 4:
    soldier = soldiers[soldierIndex]
    hero.command(soldier, "move", {"x": 50, "y": 40})
    soldierIndex = soldierIndex + 1


# Go join your comrades!
hero.moveXY(51, 41)
# hero.move(friend.pos.x, friend.pos.y)
