from collections import deque 

N, M = map(int, input().split())

start = 0
stop = 1000
q = deque()
m = 0
for i in range(N):
    current = int(input())
    start=current
    stop = start+1000
    while q:
        if q[0]+1000 <= start:
            q.popleft()
        else:
            break

    q.append(current)
    m = max(m, len(q))

print(int((m + M - 1) // M))
