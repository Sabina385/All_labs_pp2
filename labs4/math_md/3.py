import math
n=int(input("Input number of sides:"))
a=int(input("Input the length of a side:"))
area_regular_polygon = int((n * a**2)/(4*math.tan(math.pi /n)))
print("Area:",area_regular_polygon)
