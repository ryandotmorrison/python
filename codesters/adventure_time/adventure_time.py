coins = 1000
currentweapon = ""
hp = 100
hunger = 100
our_inventory = {"soup":{"hunger":50,"health":25},"first_aid_kit":{"health":95}}
basic_shop = {"katana":{"price":0,"damage":25},"pipe":{"price":0,"damage":190},"Usopp's Hat":{"price":0,"gun reload":-2},"mace":{"price":0,"damage":50},"dual katana":{"price":0,"damage":40}}
path = input("Which path do you take? Sigma or Ohio?")
if path == "Sigma":
    print("You chose Sigma.You go to the left.")
    stage.wait(1)
    print("Suddenly, a sword dealer comes out of nowhere!")
    sword = input("Do you want to browse my wares?Yes or No.")
    if sword == "Yes":
        for (k,v) in basic_shop.items():
            print(k,v)
        print(f"you have {coins} coins")
        purchase = input("Which item would you like?")
        if purchase in basic_shop:
            our_inventory[purchase] = basic_shop[purchase]
            currentweapon = purchase
            print(our_inventory)
        else:
            our_inventory["pipe"] = basic_shop["pipe"]
            currentweapon = "pipe" 
            print(our_inventory)
        print("You see a jungle.You go into the middle of the jungle.\nYou see the gorilla king.He sees you and goes bananas.\nHe has 50 hp.")
        boss = input("What do you do?Attack or Run?")
        if boss == "Attack":
            print(f"You attack.You use {currentweapon}.")
            if our_inventory[currentweapon]["damage"] >= 50:
                print("He dies at sight of your godly aura")
            else:
                print("He suffocates you with a hug so you die.\nThen, he wraps you up as a present \nand gives it to the Gorilla Queen.You Died")
        else:
            print("You Run.He catches you and kicks you to outer space.You Died.")
else:
    print("You chose Ohio.You go down the path and fall off a cliff\ninto the sharp rocks below.You Died.The End")



