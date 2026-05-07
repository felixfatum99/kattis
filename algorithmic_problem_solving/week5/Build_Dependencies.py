from collections import deque 

def kahn(name):
    S = set()
    S.add(name)
    L = []

    while S:
        n = S.pop()
        L.append(n)
        
        for m in G[n]:
            G_I[m].remove(n)
            if len(G_I[m]) == 0:
                S.add(m) 

    return L

N = int(input())
G = {}
G_I = {}

for _ in range(N):
    line = input().split()
    
    if line[0][0:-1] not in G:
        G[line[0][0:-1]] = []

    for name in line[1:]:
        if name not in G:
            G[name] = []
        
        G[name].append(line[0][0:-1])


name = input()

visited = set()
visited.add(name)
queue = deque()
queue.append(name)

while queue:
    node = queue.popleft()

    for neighbor in G[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)


for node in visited:
    G_I[node] = []

for key in G:
    for val in G[key]:
        if val in G_I and key in G_I:
            G_I[val].append(key)

order = kahn(name)

for file in order:
    print(file)