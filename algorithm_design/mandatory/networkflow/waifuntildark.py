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
    
    while BFS(g, source, sink, parent) :
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
            
    return max_flow

n, m, p = map(int, input().split(" "))
g = defaultdict(lambda: defaultdict(int))
g['sink'] = defaultdict(int)
for i in range(1, n+1):
    line = [int(t) for t in input().split(" ")]
    g['start']['child'+str(i)] = 1
    for k in range(1, line[0]+1):
        g['child'+str(i)]['toy'+str(line[k])] = 1

for i in range(1, p+1):
    p_line = [int(z) for z in input().split(" ")]
    g['cat'+str(i)]['sink'] = p_line[len(p_line)-1]
    for j in range(1, p_line[0]+1):
        g['toy'+str(p_line[j])]['cat'+str(i)] = 1

keys = g.keys()
for i in range(1, m+1):
    if 'toy'+str(i) not in keys:
        g['toy'+str(i)]['sink'] = 1

count = FordFulkerson(g, 'start', 'sink')
print(count)
