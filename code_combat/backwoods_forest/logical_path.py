# Get two secret true/false values from the wizard.
# Check the guide for notes on how to write logical expressions.
hero.moveXY(14, 24)
secretA = hero.findNearestFriend().getSecretA()
secretB = hero.findNearestFriend().getSecretB()

# If BOTH secretA and secretB are true, take the high path; otherwise, take the low path.
secretC = secretA and secretB
if secretC:
    hero.moveXY(20, 33)
else:
    hero.moveXY(20, 15)
hero.moveXY(26, 24)

# If EITHER secretA or secretB is true, take the high path.
if secretA or secretB == True:
    hero.moveXY(32, 33)
# If secretB is NOT true, take the low path.
if secretB != True:
    hero.moveXY(32, 15)
hero.moveXY(38, 24)
hero.moveXY(44, 15)
hero.moveXY(50, 24)
