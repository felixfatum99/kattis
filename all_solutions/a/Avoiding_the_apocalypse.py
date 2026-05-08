#https://open.kattis.com/problems/avoidingtheapocalypse
from collections import defaultdict, deque

INF = 100000000

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

def FordFulkerson(res, source='source', sink='sink'):
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
            if u not in res[v]:
                res[v][u] = 0
            res[v][u] += path_flow
            v = u

    return max_flow

T = int(input())

for testcase in range(T):
    town = defaultdict(lambda: defaultdict(int))

    locations = int(input())
    start, people, steps = map(int, input().split())

    #Initiate graph locations
    town['source'][(start, 0)] = people
    town['sink'] = {}

    for i in range(1, locations+1):
        for j in range(steps):
            town[(i, j)][(i, j+1)] = INF

        town[(i, steps)] = {}

    medical_facilities = int(input())
    for _ in range(medical_facilities):
        m_location = (int(input()))
        for j in range(steps+1):
            town[(m_location, j)]['sink'] = INF

    roads = int(input())
    for _ in range(roads):
        a, b, p, t = map(int, input().split())
        for j in range(steps):
            if j+t <= steps:
                town[(a, j)][(b, j+t)] = p
            else:
                break

    print(FordFulkerson(town))