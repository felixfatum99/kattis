from collections import deque

t = int(input())
for _ in range(t):
    n_stores = int(input())
    points = [tuple(map(int, input().split()))]
    for _ in range(n_stores):
        points.append(tuple(map(int, input().split()))) 
    points.append(tuple(map(int, input().split())))

    n = len(points)
    q = deque([0])
    visited = [False] * n
    visited[0] = True

    p = "sad"
    while q:
        i = q.popleft()
        if i == n - 1:
            p = "happy"
            break
        for j in range(n):
            if not visited[j] and abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]) <= 1000:
                visited[j] = True
                q.append(j)
    print(p)