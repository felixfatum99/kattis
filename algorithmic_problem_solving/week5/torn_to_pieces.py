from collections import deque

def dfs(g, src, dest):
    queue = deque()
    queue.append(src)

    parent = {src: None}
    visited = set([src])

    while queue:
        current_node = queue.pop()
        if current_node == dest:
            break

        for v in g[current_node]:
            if v not in visited:
                visited.add(v)
                parent[v] = current_node
                queue.append(v)

    if e not in parent:
        return ["no", "route", "found"]

    path = []
    cur = dest
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path


N = int(input())
G = {}

for _ in range(N):
    line = input().split()
    node = line[0]
    edges = line[1:]

    if node not in G:
        G[node] =[]
    
    for edge in edges:
        if edge not in G:
            G[edge] = []

        if edge not in G[node]:
            G[node].append(edge)
        
        if node not in G[edge]:
            G[edge].append(node)

s, e = input().split()

if s not in G or e not in G:
    print("no route found")
else:
    print(" ".join(dfs(G, s, e)))
