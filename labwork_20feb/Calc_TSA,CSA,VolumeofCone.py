# Program to calculate Curved Surface Area, Total Surface Area and Volume of a Cone

import math   # Importing math module for π (pi) and square root

# Taking input from the user
radius = float(input("Enter radius of cone: "))
height = float(input("Enter height of cone: "))

# Calculating slant height (l)
# Formula: l = √(r² + h²)
slant_height = math.sqrt(radius**2 + height**2)

# Calculating Curved Surface Area (CSA)
# Formula: π * r * l
curved_surface_area = math.pi * radius * slant_height

# Calculating Total Surface Area (TSA)
# Formula: π * r * (r + l)
total_surface_area = math.pi * radius * (radius + slant_height)

# Calculating Volume
# Formula: (1/3) * π * r² * h
volume = (1/3) * math.pi * radius**2 * height

# Displaying the results
print("\n--- Results ---")
print("Slant Height:", slant_height)
print("Curved Surface Area (CSA):", curved_surface_area)
print("Total Surface Area (TSA):", total_surface_area)
print("Volume:", volume)
