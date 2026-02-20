# three_d_shapes.py
# Module for operations on 3D figures

import math

# ------------------- CUBE -------------------

def cube_volume(side):
    """Calculate volume of cube"""
    return side ** 3

def cube_surface_area(side):
    """Calculate surface area of cube"""
    return 6 * (side ** 2)


# ------------------- CUBOID -------------------

def cuboid_volume(length, breadth, height):
    """Calculate volume of cuboid"""
    return length * breadth * height

def cuboid_surface_area(length, breadth, height):
    """Calculate surface area of cuboid"""
    return 2 * (length*breadth + breadth*height + height*length)


# ------------------- CYLINDER -------------------

def cylinder_volume(radius, height):
    """Calculate volume of cylinder"""
    return math.pi * (radius ** 2) * height

def cylinder_surface_area(radius, height):
    """Calculate surface area of cylinder"""
    return 2 * math.pi * radius * (radius + height)


# ------------------- CONE -------------------

def cone_volume(radius, height):
    """Calculate volume of cone"""
    return (1/3) * math.pi * (radius ** 2) * height

def cone_surface_area(radius, height):
    """Calculate surface area of cone"""
    slant_height = math.sqrt(radius**2 + height**2)
    return math.pi * radius * (radius + slant_height)


# ------------------- SPHERE -------------------

def sphere_volume(radius):
    """Calculate volume of sphere"""
    return (4/3) * math.pi * (radius ** 3)

def sphere_surface_area(radius):
    """Calculate surface area of sphere"""
    return 4 * math.pi * (radius ** 2)


# ------------------- HEMISPHERE -------------------

def hemisphere_volume(radius):
    """Calculate volume of hemisphere"""
    return (2/3) * math.pi * (radius ** 3)

def hemisphere_surface_area(radius):
    """Calculate surface area of hemisphere (including base)"""
    return 3 * math.pi * (radius ** 2)


#---------------------MODULEs----------------------------
import three_d_shapes as tds
# Cube
print("Cube Volume:", tds.cube_volume(4))
print("Cube Surface Area:", tds.cube_surface_area(4))

# Cylinder
print("Cylinder Volume:", tds.cylinder_volume(3, 5))

# Sphere
print("Sphere Surface Area:", tds.sphere_surface_area(2))
