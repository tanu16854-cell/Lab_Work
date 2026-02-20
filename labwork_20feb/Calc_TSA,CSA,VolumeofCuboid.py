# Program to calculate Curved Surface Area, Total Surface Area and Volume of a Cuboid

# Taking input from the user
length = float(input("Enter length of cuboid: "))
breadth = float(input("Enter breadth of cuboid: "))
height = float(input("Enter height of cuboid: "))

# Calculating Curved Surface Area (CSA)
# Formula: 2 * height * (length + breadth)
curved_surface_area = 2 * height * (length + breadth)

# Calculating Total Surface Area (TSA)
# Formula: 2 * (lb + bh + hl)
total_surface_area = 2 * (length * breadth + breadth * height + height * length)

# Calculating Volume
# Formula: length * breadth * height
volume = length * breadth * height

# Displaying the results
print("\n--- Results ---")
print("Curved Surface Area (CSA):", curved_surface_area)
print("Total Surface Area (TSA):", total_surface_area)
print("Volume:", volume)
