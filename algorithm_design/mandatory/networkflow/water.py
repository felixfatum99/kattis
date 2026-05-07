from collections import defaultdict

def BFS(g, r, s, t, parent):
        visited = {i: False for i in g.keys()}
        
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)

            for ind in g[u].keys():
                if visited[ind] == False and g[u][ind]> 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True

        return False
             
def FordFulkerson(g,r, source, sink):
    parent = {i: -1 for i in g.keys()}

    max_flow = 0 

    while BFS(g, r, source, sink, parent) :
        path_flow = float("Inf")
        s = sink
        while(s !=  source):
            path_flow = min (path_flow, g[parent[s]][s])
            s = parent[s]

        max_flow +=  path_flow

        v = sink
        while(v !=  source):
            u = parent[v]
            g[u][v] -= path_flow
            g[v][u] += path_flow
            v = parent[v]
        
    return max_flow


n, p, k = map(int, input().split(" "))
g = defaultdict(lambda: defaultdict(int))

for i in range(p):
    a, b, c = map(int, input().split(" "))
    g[a][b] = c
    g[b][a] = c

res = FordFulkerson(g, len(g), 1, 2)
print(res)

for i in range(k):
    a, b, c = map(int, input().split(" "))
    if a in g.keys():
        if b not in g[a].keys():
            g[a][b] = c
            g[b][a] = c
        else:
            g[a][b] += c
            g[b][a] += c
    else:
        g[a][b] = c
        g[b][a] = c
    res += FordFulkerson(g, len(g), 1, 2)
    print(res)
