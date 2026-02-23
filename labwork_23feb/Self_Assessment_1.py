# -------------------------------
# ONLINE GROCERY STORE PROJECT
# -------------------------------

# ---------- LIST ----------
# List of available grocery items
items = ["milk", "bread", "rice", "sugar", "oil", "eggs"]

# ---------- TUPLE ----------
# Prices of items (fixed values - cannot change)
prices = (50, 30, 60, 45, 120, 70)

# ---------- DICTIONARY ----------
# Mapping items with prices
grocery_dict = {
    "milk": 50,
    "bread": 30,
    "rice": 60,
    "sugar": 45,
    "oil": 120,
    "eggs": 70
}

# ---------- SET ----------
# To store unique items selected by user
cart = set()

# ---------- STRING ----------
# Welcome message
print("\n===== Welcome to Online Grocery Store =====\n")

# Display available items
print("Available Items:")
for item in items:
    print("-", item)

print("\n--------------------------------------")

# Taking user input
choice = input("Enter items to add in cart (comma separated): ")

# Convert string input to list
user_items = choice.lower().split(",")

# Add items to cart (SET automatically removes duplicates)
for i in user_items:
    item = i.strip()
    if item in items:
        cart.add(item)
    else:
        print(f"{item} is not available!")

print("\nYour Cart Items:", cart)

# Calculate total bill
total = 0
for item in cart:
    total += grocery_dict[item]

print("\nTotal Bill =", total)

print("\n===== Thank You for Shopping! =====")
