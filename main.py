import random
import math

class point:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num

def point_dist(p1, p2):
    x1 = p1.x
    y1 = p1.y
    x2 = p2.x
    y2 = p2.y
    distance = math.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2 )
    return distance

def randPoints(num):
    points =[]
    for x in range(num):
        p = point(random.randint(0, 1000), random.randint(0, 1000), x)
        points.append(p)
    return points

num = input("Input an Int.")
num = int(num)

points = randPoints(num)
points = list(points)
for x in range(num):
    for z in range(num):
        print(f"distance between point{x} and {z}: {point_dist(points[x], points[z])}")

