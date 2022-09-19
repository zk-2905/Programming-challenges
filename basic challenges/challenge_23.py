length = float(input("Enter the length of the garden in metres: "))
width = float(input("Enter the width of the garden in metres: "))
radius = float(input("Enter the radius of the circular flower bed in meters: "))

def flower_bed(radius):
    return (radius**2)*3.14
circle_area = flower_bed(radius)

def garden():
    return length * width
garden_area = garden()

turf_needed = garden_area-circle_area
print(f"{turf_needed} metres")