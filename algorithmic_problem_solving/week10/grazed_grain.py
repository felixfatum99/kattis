import random

n = int(input())
c = []
min_x, max_x, min_y, max_y = float('inf'), -float('inf'), float('inf'), -float('inf')

for _ in range(n):
    x, y, r = map(int, input().split())
    min_x = min(min_x, x-r)
    max_x = max(max_x, x+r)
    min_y = min(min_y, y-r)
    max_y = max(max_y, y+r)
    c.append((x, y, r))

a = (max_x - min_x) * (max_y - min_y)

s = 10000
i = 0

for _ in range(s):
    rx = random.uniform(min_x, max_x)
    ry = random.uniform(min_y, max_y)
    for x, y, r in c:
        dx = rx - x
        dy = ry - y
        if dx*dx + dy*dy <= r*r:
            i += 1
            break

print(a * i / s)