from cmath import sqrt
import math

r = float(input("Enter the length from the center to a vertex : "))
s = 2*r*math.sin(math.pi/5)
area = float(round(3*math.sqrt(3)/2*pow(s,2),2))

print("The area of the pentagon is", area)
