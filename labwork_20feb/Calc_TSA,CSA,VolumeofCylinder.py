# Program to calculate Curved Surface Area, Total Surface Area and Volume of a Cylinder

import math   # Importing math module for π (pi)

# Taking input from the user
radius = float(input("Enter radius of cylinder: "))
height = float(input("Enter height of cylinder: "))

# Calculating Curved Surface Area (CSA)
# Formula: 2 * π * r * h
curved_surface_area = 2 * math.pi * radius * height

# Calculating Total Surface Area (TSA)
# Formula: 2 * π * r * (r + h)
total_surface_area = 2 * math.pi * radius * (radius + height)

# Calculating Volume
# Formula: π * r² * h
volume = math.pi * (radius ** 2) * height

# Displaying the results
print("\n--- Results ---")
print("Curved Surface Area (CSA):", curved_surface_area)
print("Total Surface Area (TSA):", total_surface_area)
print("Volume:", volume)
