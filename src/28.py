def calculate_volume(cylinder_radius, cylinder_height):
    volume = 3.14 * cylinder_radius ** 2 * cylinder_height
    return volume

cylinder_radius = 5
cylinder_height = 10
result = calculate_volume(cylinder_radius, cylinder_height)
print(f"The volume of the cylinder is: {result}")
