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

n = int(input())
g = defaultdict(lambda: defaultdict(int))
g['sink'] = defaultdict(int)
correct_order = []

for i in range(n):
    a, b = map(int, input().split())
    correct_order.append((a, b))

    g['start'][(a, b)] += 1
    prod, summ, sub = a * b, a - b, a + b
    g[(a, b)][prod] = 1
    g[(a, b)][sub] = 1
    g[(a, b)][summ] = 1
    g[summ]['sink'] = 1
    g[prod]['sink'] = 1
    g[sub]['sink'] = 1

count = FordFulkerson(g, 'start', 'sink', n)

if count < n:
    print("impossible")
else:
    for pair in correct_order:
        for res in g[pair].keys():
            if g[pair][res] == 0:
                a, b = pair
                if a + b == res:
                    print(f"{a} + {b} = {res}")
                elif a - b == res:
                    print(f"{a} - {b} = {res}")
                else:
                    print(f"{a} * {b} = {res}")
                g[pair][res] = 1
                break
