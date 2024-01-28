# Move in sync with your dance partner to impress Pender Spellbane.
friend = hero.findNearest(hero.findFriends())
diffx = friend.pos.x - hero.pos.x
diffy = friend.pos.y - hero.pos.y
while True:
    target = {'x': friend.pos.x - diffx, 'y': friend.pos.y - diffy}
    hero.move(target)
