def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points

    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]

def polygon_area(poly):
    n = len(poly)
    if n < 3:
        return 0.0
    s = 0
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i+1) % n]
        s += x1 * y2 - x2 * y1
    return abs(s) / 2.0


while True:
    n = int(input())
    if n == 0:
        break

    points = []
    for i in range(n):
        beacon_x, beacon_y = map(int, input().split())
        points.append((beacon_x, beacon_y))

    print(polygon_area(convex_hull(points)))
