# calculate area and circumference

import math

def circle_stats(r):
    area = math.pi * r ** 2
    circumference = 2 * math.pi * r
    return area , circumference

a,c = circle_stats(3)
print("area :", a)
print("circumference : ",c)