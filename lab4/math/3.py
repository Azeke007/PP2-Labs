import math
num_sides = int(input("Enter the number of sides of the polygon: "))
side_length = float(input("Enter the length of each side: "))

apothem_length = side_length / (2 * math.tan(math.pi / num_sides))
area = 0.5 * apothem_length * num_sides * side_length

print(f"The area of the regular polygon is {area}.")
