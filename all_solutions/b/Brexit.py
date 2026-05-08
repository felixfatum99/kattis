#https://open.kattis.com/problems/brexit
from collections import deque

C, P, X, L = map(int, input().split())

d = {}

for i in range(P):
    a, b = map(int, input().split())
    if a in d:
        d[a].append(b)
    else:
        d[a] = [b]
    
    if b in d:
        d[b].append(a)
    else:
        d[b] = [a]

d_d = {}
for key in d:
    length = len(d[key]) if len(d[key]) % 2 == 0 else len(d[key]) + 1
    d_d[key] = [length, length]

if X == L:
    print("leave")
else:
    visited = set()
    q = deque()
    q.append(L)
    visited.add(L)

    while q:
        leaving = q.popleft()

        for val in d[leaving]:
            d_d[val][0] -= 1
            if d_d[val][0] <= d_d[val][1]/2:
                if val not in visited:
                    visited.add(val)
                    q.append(val)
    
    
    if d_d[X][0] <= d_d[X][1]/2:
        print("leave")
    else:
        print("stay")