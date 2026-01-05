import json
import os
# this is to add a new product to the inventory
def add_item(inventory):
    print("\n- Add new Coffe/Tea item to inventory- ")
#showing all avaalible items
    print("item: Latte , Cappuchino , Frapupuccino , Black coffe , Tea ,Green Tea")
    item_id = input("enter item ID (e.g , L1 ,  C1 , F1 , B1, T1, GT1 )")
    if item_id in inventory:
        print("item ID already exists")
        return

name = input("enter the name of the item"), strip()
category = input("enter category ( Latte/Cappucino/Frappuccino/Black coffe/Tea/Green Tea):").strip()
quality = input("enter quality (cups/servings):").strip()
price = input("enter price per servings: £").strip()
size = input("enter size (small/medium/large): ") .strip()

try:
    #converting quantity from a string to integer
    quantity = int(quantity)
    #convert price from string to decimal number
    price = float(price)
except ValueError:
    #this is to show error and stop adding the item
    print("invalid quantity or price. item hasnt been added")
    return
#adding the new item to the inventory usig item_id as the key
inventory[item_id] = {
    "name" : name,
    "category": category,
    "quantitiy": quantity,
    "price": price,
    "size": size
}
#conformation the user has added the item
print(f"item '{name} ' added")
