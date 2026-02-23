# E-Commerce Cart System
# This program:
# 1. Removes duplicate product prices
# 2. Calculates total amount
# 3. Applies 10% discount if total > 5000
# 4. Adds 18% GST
# 5. Displays final payable amount

#List of product prices (cart)
cart_prices = [1200, 2500, 1200, 800, 1500, 2500]

#Remove duplicate prices
unique_prices = []

for price in cart_prices:
    if price not in unique_prices:
        unique_prices.append(price)

print("Unique Product Prices:", unique_prices)
print("--------------------------------------")
#Calculate total amount
total = sum(unique_prices)
print("Total Amount (Before Discount):", total)
print("--------------------------------------")
#Apply discount if total > 5000
if total > 5000:
    discount = total * 0.10   # 10% discount
    total_after_discount = total - discount
    print("Discount Applied:", discount)
else:
    total_after_discount = total
    print("No Discount Applied")

print("Amount After Discount:", total_after_discount)
print("--------------------------------------")
#Add GST (18%)
gst = total_after_discount * 0.18
final_amount = total_after_discount + gst

print("GST (18%):", gst)
print("Final Payable Amount:", final_amount)
print("--------------------------------------")
