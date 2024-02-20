# Input number of sides: 4
# Input the length of a side: 25
# The area of the polygon is: 625

import math
n = int(input("Input number of sides: "))
side = float(input("Input the length of a side: "))
apothem = side/(2 * math.tan(math.pi/n))
area = 0.5 * (n * side) * apothem
print("The area of the polygon is: {:.0f}".format(area))
