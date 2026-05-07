import math
def find_area(cp, points):
    area = 0
    for i in range(len(points)):
        if i == len(points)-1:
            d1 = math.dist(cp, points[i])
            d2 = math.dist(cp, points[0])
            d3 = math.dist(points[i], points[0])
            area += areaTriangle(d1, d2, d3)
        else:
            d1 = math.dist(cp, points[i])
            d2 = math.dist(cp, points[i+1])
            d3 = math.dist(points[i], points[i+1])
            area += areaTriangle(d1, d2, d3)
    return area 

def areaTriangle(a, b, c):
    s = (a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5

t = int(input())
for _ in range(t):
    info = [int(x) for x in input().split()]
    min_x, max_x = float('inf'), -5001
    min_y, max_y = float('inf'), -5001
    points = []
    for j in range(1, info[0]*2, +2):
        x = info[j]
        y = info[j+1]
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        points.append((x, y))
    
    cp_x = ((max_x-min_x)/2)+min_x
    cp_y = ((max_y-min_y)/2)+min_y
    area = find_area((cp_x, cp_y), points)
    print(int(area))