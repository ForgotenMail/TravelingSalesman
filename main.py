import random
import math

class point:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num
        
    def __repr__(self):
        return f"Point({self.num}, {self.x}, {self.y})"
class path:
    def __init__(self, points):
        self.points = points
        self.cost = 0
        for x in range(len(points)):
            y = x -1
            self.cost += point_dist(points[x], points[y])

    def __repr__(self):
        return f"path(points={self.points}, cost={self.cost})"
    def len(self):
        return len(points)

        

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

def pointDist(p1, p2):
    return (math.sqrt((p2.x - p1.x)**2) + math.sqrt((p2.y-p1.y)**2))



## I have no idea right now whether the loop is actually working, so We need to check that
def bruteForce(points):
    print("Entered BruteForce Loop")
    numPoints = len(points)
    bruteList = list([])
    for x in range(numPoints - 1):
        bruteList.append(0)
    pathScore = int()
    bestPath = []
    while True:
        availiblePoints = points.copy()
        Trace = list([])
        for x in range(numPoints - 1):
            augment =  bruteList[x]
            index = int(augment)
            Trace.append(availiblePoints.pop(index))
        score = 0
        Trace.append(availiblePoints[0])
        for x in range(len(Trace)):
            score += pointDist(Trace[x], Trace[x-1])
        if score < pathScore or pathScore == 0:
            pathScore = score
            bestPath = Trace
        
        incr = increment(bruteList)
        if  incr == "finished":
            return bestPath
        else:
            if incr != None:
                bruteList = incr


def increment(a, i=None):
    if i is None:
        i = len(a) - 1

    if a[i] < len(a) - i:
        a[i] += 1
        if i == 0 and a[i] == len(a):
            return "finished"
        return a

    a[i] = 0

    if i == 0:
        return 

    return increment(a, i - 1)


        
num = input("Input an Int.")
num = int(num)

# points = randPoints(num)
# points = list(points)
# for x in range(num):
#     for z in range(num):
#         print(f"distance between point{x} and {z}: {point_dist(points[x], points[z])}")
#

points = [
        point(0,0, 0), 
        point(1,5,1), 
        point(3,6,2), 
        point(6, 5, 3),
        point(7, 0, 4),
        point(3.5,2.5,5)
        ]

Path = path(bruteForce(points))
print(Path)
print(Path.cost)


