products: list = ["Item1", "Item2", "Item3", "Item4"]

basket: list = []

print("This is our products")
print(products)

command: str = input("Please choose command: (add, remove, exit, clear)")

while command != "exit":
    if command == "add":
        item_name: str = input("please enter your item name:")

        if item_name in products:
            basket.append(item_name)
            print("You product added to your basket successfully")
        else:
            print("We don't have this product in our inventory")

        print()
        print("\nYour basket")
        for (index, item) in enumerate(basket, start=1):
            print(f"{index} {item}")
    elif command == "remove":
        print("remove an item")
    elif command == "clear":
        basket.clear()
        print("clear basket")
    command: str = input("Please choose command: (add, remove, exit, clear)")


