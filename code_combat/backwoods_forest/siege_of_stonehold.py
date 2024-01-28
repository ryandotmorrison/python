# Help your friends beat the minions that Thoktar sends against you.
# You'll need great equipment and strategy to win.
# Flags might help, but it's up to you–be creative!
# There is a doctor behind the fence. Move to the X to get healed!
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
    else:
        hero.moveXY(19, 69)
