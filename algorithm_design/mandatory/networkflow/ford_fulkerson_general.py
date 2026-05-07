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

def main():
    g = defaultdict(lambda: defaultdict(int))

main()
