from collections import defaultdict, deque

def BFS(g, s, t, parent):
    visited = {i: False for i in g.keys()}
    queue = deque([s])
    visited[s] = True

    while queue:
        u = queue.popleft()
        for ind in g[u]:
            if not visited[ind] and g[u][ind] > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
                if ind == t:
                    return True

    return False

def FordFulkerson(g, source, sink):
    parent = {i: -1 for i in g.keys()}
    max_flow = 0 
    
    while BFS(g, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while(s !=  source):
            path_flow = min (path_flow, g[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = sink
        while(v !=  source):
            u = parent[v]
            g[u][v] -= path_flow
            g[v][u] += path_flow
            v = parent[v]
            
    return g

graph = defaultdict(lambda: defaultdict(int))
n, m, s, t = map(int, input().split())

for i in range(n):
    graph[i] = defaultdict(int)

for j in range(m):
    u, v, w = map(int, input().split())
    graph[u][v] = w
    graph[v][u] += 0

residual_graph = FordFulkerson(graph, s, t)

k = 0
nodes = []
q = deque()
q.append(s)
visited = set()
visited.add(s)

while q:
    node = q.popleft()
    k+=1
    nodes.append(node)

    for key in residual_graph[node]:
        if residual_graph[node][key] > 0:
            if key not in visited:
                q.append(key)
                visited.add(key)

print(k)
for val in nodes:
    print(val)


