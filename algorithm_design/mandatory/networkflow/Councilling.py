from collections import defaultdict, deque

def BFS(g, s, t, parent):
    visited = set()
    queue = deque([s])
    visited.add(s)

    while queue:
        u = queue.popleft()
        for v, capacity in g[u].items():
            if v not in visited and capacity > 0:
                queue.append(v)
                visited.add(v)
                parent[v] = u
                if v == t:
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
        if max_flow >= n:
            return max_flow

    return max_flow

for t in range(int(input())):
    g = defaultdict(lambda: defaultdict(int))
    g['sink'] = defaultdict(int)

    n = int(input())
    names = []
    distinct_clubs = set()
    distinct_parties = set()

    for i in range(n):
        info = [s for s in input().split()]
        R = info[0]
        names.append(R)
        P = info[1]
        distinct_parties.add(P)
        g[R][P] = 1
        for j in range(3, int(info[2])+3):
            club = info[j]
            distinct_clubs.add(club)
            g[club][R] = 1
            g['start'][club] = 1

    council_amount = len(distinct_clubs)
    cutoff = council_amount//2 if council_amount%2==1 else (council_amount//2)-1
    for party in distinct_parties:
        g[party]['sink'] = cutoff

    count = FordFulkerson(g, 'start', 'sink', council_amount)
    if count < council_amount:
        print("Impossible.")
    else:
        for n in names:
            for c in distinct_clubs:
                if c in g[n].keys() and g[n][c] == 1:
                    print(n, c)

