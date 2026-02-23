# Remove duplicate products from shopping cart

cart = ["apple", "banana", "apple", "milk", "banana"]

unique_cart = []

for item in cart:
    if item not in unique_cart:
        unique_cart.append(item)

print("Unique Items:", unique_cart)
