n, m = map(int, input().split())

events = []

for _ in range(n):
    b, d = map(int, input().split())
    t = b
    while t < m:
        end = t + d
        if t < m:
            events.append((t, +1))
        if end < m:
            events.append((end, -1))
        t += b + d

events.sort(key=lambda x: (x[0], x[1]))

curr = 0
max_restrooms = 0

for _, change in events:
    curr += change
    max_restrooms = max(max_restrooms, curr)

print(max_restrooms)
