import math
import sys

def points():
    input = sys.stdin.read
    data = input().split()

    idx = 0
    results = []
    
    while True:
        n = int(data[idx])
        idx += 1
        if n == 0:
            break
        
        p = [(float(data[idx + 2 * i]), float(data[idx + 2 * i + 1])) for i in range(n)]
        idx += 2 * n
        
        p.sort(key=lambda point: point[0]) 
        dist, closest_points = closest_recursive(p, n)
        results.append(f"{closest_points[0][0]} {closest_points[0][1]} {closest_points[1][0]} {closest_points[1][1]}")
    
    sys.stdout.write("\n".join(results) + "\n")

    
def closest_recursive(points, n):
    if n <= 3:
        dist, ps = bf(points, n)
        return dist, ps 
    half = n//2
    half_point = points[half]

    go_left = closest_recursive(points[:half], half) 
    go_right = closest_recursive(points[half:], n-half)

    if go_left[0] < go_right[0]:
        m = go_left[0]
        mp = go_left[1]
    else:
        m = go_right[0]
        mp = go_right[1]

    rest = []
    for i in range(n):
        if abs(points[i][0] - half_point[0]) < m:
            rest.append(points[i])
    
    check_on_y = y_sort(rest, m, mp)
    if m < check_on_y[0]:
        return m, mp
    else:
        return check_on_y

def bf(points, n):
    d1 = math.sqrt((points[0][0]-points[1][0])**2+(points[0][1]-points[1][1])**2)
    if n == 3:
        d2 = math.sqrt((points[0][0]-points[2][0])**2+(points[0][1]-points[2][1])**2)
        d3 = math.sqrt((points[1][0]-points[2][0])**2+(points[1][1]-points[2][1])**2)
        if d1 < d2 and d1 < d3:
            return d1, [points[0], points[1]]
        if d2 < d1 and d2 < d3:
            return d2, [points[0], points[2]]
        else:
            return d3, [points[1], points[2]]
    else:
        return d1, [points[0], points[1]]


def y_sort(rest, d, mp):
    min_dist = d
    min_points = mp
    rest.sort(key=lambda point: point[1])
 
    for i in range(len(rest)):
        for j in range(i+1, min(i+7,len(rest))):
            if (rest[j][1] - rest[i][1]) >= min_dist:
                break
            if math.sqrt((rest[j][0]-rest[i][0])**2+(rest[j][1]-rest[i][1])**2) < min_dist:
                min_dist = math.sqrt((rest[j][0]-rest[i][0])**2+(rest[j][1]-rest[i][1])**2)
                min_points = [rest[i], rest[j]]
    return min_dist, min_points

points()