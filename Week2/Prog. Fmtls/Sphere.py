import math 

diameter = float(input("what is the diameter?"))

radius = diameter / 2
area = 4*math.pi*(radius*radius)
volume=(4/3)*math.pi*pow(radius,3)

print(f"the radius is {radius} the area is {area} and the volume is {volume}")
