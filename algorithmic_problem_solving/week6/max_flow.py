from copy import deepcopy
from collections import defaultdict, deque

def BFS(g, s, t, parent):
    visited = set([s])
    q = deque([s])
    parent.clear()
    parent[s] = None

    while q:
        u = q.popleft()
        for v, cap in g[u].items():
            if v not in visited and cap > 0:
                visited.add(v)
                parent[v] = u
                if v == t:
                    return True
                q.append(v)
    return False

def FordFulkerson(res, source, sink):
    parent = {}
    max_flow = 0

    while BFS(res, source, sink, parent):
        path_flow = float("inf")
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, res[u][v])
            v = u

        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            res[u][v] -= path_flow
            res[v][u] += path_flow
            v = u

    return max_flow

g = defaultdict(lambda: defaultdict(int))
n, m, s, t = map(int, input().split())

for _ in range(m):
    u, v, c = map(int, input().split())
    g[u][v] += c
    g[v]

orig = deepcopy(g)
res = g

maxflow = FordFulkerson(res, s, t)

flow = defaultdict(dict)
for u in orig:
    for v, cap in orig[u].items():
        f = cap - res[u][v]
        if f > 0:
            flow[u][v] = f

_m = 0

for key in flow:
    _m += len(flow[key])

print(n, maxflow, _m)

for key in flow:
    for k in flow[key]:
        print(key, k, flow[key][k])