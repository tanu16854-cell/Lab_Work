# Inventory Management System
# This program:
# 1. Removes items with 0 stock
# 2. Adds restock of 50 units to items below 10
# 3. Calculates total inventory count

#List of product stock quantities
stock = [0, 5, 20, 8, 0, 15, 3]

#Remove items with 0 stock
valid_stock = []

for qty in stock:
    if qty > 0:              # keep only items with stock > 0
        valid_stock.append(qty)

print("Stock after removing 0 quantity items:", valid_stock)
print("--------------------------------------")

#Add restock of 50 units to items below 10
updated_stock = []

for qty in valid_stock:
    if qty < 10:
        qty = qty + 50       # restock
    updated_stock.append(qty)

print("Stock after restocking:", updated_stock)
print("--------------------------------------")

#Calculate total inventory count
total_inventory = sum(updated_stock)

print("Total Inventory Count:", total_inventory)
print("--------------------------------------")
