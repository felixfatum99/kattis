import sys
from collections import defaultdict, deque

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


lines = sys.stdin.read().splitlines()
i = 0

while i < len(lines):
    g = defaultdict(lambda: defaultdict(int))
    m, n = map(int, lines[i].split())
    i += 1

    for k in range(m):
        g[k] = {}
    
    for j in range(n):
        a, b = map(int, lines[i].split())
        g[a][b] = 1
        i += 1


