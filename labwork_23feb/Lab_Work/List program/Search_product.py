# Search item in product list

products = ["laptop", "mobile", "tablet", "camera"]

search = input("Enter product to search: ")

if search in products:
    print("Product Found")
else:
    print("Product Not Found")
