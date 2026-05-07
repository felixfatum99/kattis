from collections import defaultdict, deque

def BFS(g, s, t, parent):
    visited = set()
    queue = deque([s])
    visited.add(s)

    while queue:
        u = queue.popleft()
        for ind in g[u]:
            if ind not in visited and g[u][ind] > 0:
                queue.append(ind)
                visited.add(ind)
                parent[ind] = u
                if ind == t:
                    return True
    return False

def FordFulkerson(g, source, sink, n):
    parent = {}
    max_flow = 0 
    
    while BFS(g, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, g[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            g[u][v] -= path_flow
            g[v][u] += path_flow
            v = parent[v]
        
        if max_flow == n:
            return max_flow
                
    return max_flow

N, M = map(int, input().split())
if N > M:
    print("Impossible")
    exit()
g = defaultdict(lambda: defaultdict(int))
g['sink'] = defaultdict(int)

for i in range(M):
    a, b = map(int, input().split())
    shooter_a = 'shooter'+str(a)
    target_a = 'target'+str(a)
    shooter_b = 'shooter'+str(b)
    target_b = 'target'+str(b)

    g['start'][shooter_a] = 1
    g['start'][shooter_b] = 1

    g[shooter_a][target_b] = 1
    g[shooter_b][target_a] = 1
    g[target_a]['sink'] = 1
    g[target_b]['sink'] = 1

count = FordFulkerson(g, 'start', 'sink', N)
if count < N:
    print("Impossible")
else:
    for i in range(1, N+1):
        shooter = 'shooter'+str(i)
        for v in g[shooter].keys():
            if g[shooter][v] == 0:
                print(v[6:])