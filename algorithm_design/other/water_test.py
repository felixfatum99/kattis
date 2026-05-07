from collections import defaultdict

def BFS(g, r, s, t, parent):
    visited = {i: False for i in range(1, r + 1)}
    queue = []
    
    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.pop(0)

        for ind in g[u].keys():
            if not visited[ind] and g[u][ind] > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
                if ind == t:
                    return True

    return False

def FordFulkerson(g, r, source, sink):
    parent = {i: -1 for i in range(1, r + 1)}
    max_flow = 0

    while BFS(g, r, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, g[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            g[u][v] -= path_flow  # Decrease the capacity in the original graph
            g[v][u] += path_flow  # Increase the capacity in the reverse graph
            v = parent[v]

    return max_flow

n, p, k = map(int, input().split(" "))
g = defaultdict(lambda: defaultdict(int))

# Read initial pipes
for _ in range(p):
    a, b, c = map(int, input().split(" "))
    g[a][b] += c  # Allow multiple edges between the same nodes
    g[b][a] += c

# Initial maximum flow
print(FordFulkerson(g, len(g), 1, 2))

# Process improvements
for _ in range(k):
    a, b, c = map(int, input().split(" "))
    if a in g.keys():
        if b not in g[a].keys():
            g[a][b] += c
            g[b][a] += c  # Ensure undirected capacity is updated
        else:
            g[a][b] += c
            g[b][a] += c
    else:
        g[a][b] += c
        g[b][a] += c
    
    # Print maximum flow after the improvement
    print(FordFulkerson(g, len(g), 1, 2))
