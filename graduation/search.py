class Shopkeeper:
    def __init__(self, shop_name, inventory):
        self.shop_name = shop_name
        self.inventory = inventory

    def greet_customer(self):
        print(f"Welcome to {self.shop_name}!")

    def list_items(self):
        print("\nItems in stock:")
        for item, price in self.inventory.items():
            print(f"- {item}: ${price:.2f}")

    def take_order(self):
        order = input("\nWhat would you like to buy? ").lower()

        # Find the item without worrying about capitalization
        for item in self.inventory:
            if item.lower() == order:
                return item

        print("Sorry, we don't have that item.")
        return None

    def charge_customer(self, item):
        price = self.inventory[item]
        print(f"\nThat will be ${price:.2f}.")
        print(f"Thank you for shopping at {self.shop_name}!")
        print("Have a good day!")

        return price

shop = Shopkeeper(
    "Fiona's Grocery Store",
    {
        "Apple": 1.00,
        "Banana": 0.75,
        "Bread": 3.50,
        "Milk": 4.00
    }
)

shop.greet_customer()

while True:
    print("\nWhat would you like to do?")
    print("1. See items")
    print("2. Buy something")
    print("3. Leave")

    choice = input("Enter your choice: ")

    if choice == "1":
        shop.list_items()

    elif choice == "2":
        item = shop.take_order()

        if item is not None:
            shop.charge_customer(item)
            break

    elif choice == "3":
        print("Thanks for visiting! Have a good day!")
        break

    else:
        print("Please enter 1, 2, or 3.")