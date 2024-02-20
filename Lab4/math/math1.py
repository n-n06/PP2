import math


deg = float(input("Input degree: "))
print("Output radian: {:.6f}".format(math.radians(deg)))


rad = (deg * math.pi) / 180.0
print("Output radian: {:.6f}".format(rad))