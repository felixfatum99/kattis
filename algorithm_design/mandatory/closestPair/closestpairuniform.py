import math


def points():
    n = 1
    while n != 0:
        n = int(input())
        if n == 0:
            break
        p = []

        for i in range(n):
            x, y = map(float, input().split(" "))
            p.append((x, y))

        p.sort()
        dist, points = closest_recursive(p, n)
        print(points[0][0], points[0][1], points[1][0], points[1][1])
    
def closest_recursive(points, n):
    if n <= 3:
        dist, ps = brute_force(points, n)
        return dist, ps 
    half = n//2
    half_point = points[half]

    go_left = closest_recursive(points[:half], half) 
    go_right = closest_recursive(points[half:], n-half)
    m = 0
    mp = [(0, 0), (0, 0)]
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
    
    check_on_y = y_sort(rest, len(rest), m, mp)
    if m < check_on_y[0]:
        return m, mp
    else:
        return check_on_y

def euclidean_dist(p1, p2):
    return math.sqrt((abs(p2[0]-p1[0])**2)+(abs(p2[1]-p1[1])**2))

def brute_force(points, n):
    min_dist = float("inf")
    min_points = [(0, 0), (0, 0)]
    for i in range(n):
        for j in range(i+1, n):
            if euclidean_dist(points[i], points[j]) < min_dist:
                min_dist = euclidean_dist(points[i], points[j])
                min_points[0] = points[i]
                min_points[1] = points[j]
    return min_dist, min_points

def y_sort(rest, n, d, mp):
    min_dist = d
    min_points = mp
    rest = sorted(rest, key=lambda point: point[1])
 
    for i in range(n):
        for j in range(i+1, n):
            if (rest[j][1] - rest[i][1]) >= min_dist:
                break
            if euclidean_dist(rest[i], rest[j]) < min_dist:
                min_dist = euclidean_dist(rest[i], rest[j])
                min_points[0] = rest[i]
                min_points[1] = rest[j]
    return min_dist, min_points

points()