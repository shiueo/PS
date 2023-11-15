import math
import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())
centroid_x, centroid_y = (a+c+e)/3, (b+d+f)/3

area = abs(a*d+c*f+e*b-c*b-d*e-f*a)/2

V_x, V_y = 2*math.pi*centroid_y*area, 2*math.pi*centroid_x*area
print(V_x, V_y)