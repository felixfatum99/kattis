N, T = map(int, input().split())
queue = []

for _ in range(N):
    c_i, t_i = map(int, input().split())
    queue.append((c_i, t_i))

queue.sort(key=lambda element: (-element[0], -element[1]))
slots = [0] * (T + 1)

for c, t in queue:
    for i in range(t, -1, -1):
        if slots[i] == 0:
            slots[i] = c
            break

print(sum(slots))