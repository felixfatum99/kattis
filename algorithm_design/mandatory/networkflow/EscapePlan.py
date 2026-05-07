from collections import defaultdict, deque
import math

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

def can_reach(c1, c2, s):
    dist = math.dist(c1, c2)
    return 10 * s >= dist

scenario = 0
while True:
    g = defaultdict(lambda: defaultdict(int))
    g['sink'] = defaultdict(int)
    scenario += 1

    m = int(input()) 
    if m == 0:
        break
    
    robots = []
    for i in range(m):
        x, y = map(float, input().split())
        robots.append((x, y))
        robot = f'robot{i}'
        g['start'][robot] = 1

    
    n = int(input())
    holes = []
    for i in range(n):
        x, y = map(float, input().split())
        holes.append((x, y))
        hole = f'hole{i}'
        g[hole]['sink'] = 1

    print("Scenario", scenario)
    
    s = 5
    max_flow = 0
    for x in range(3):
        for i in range(m):
            for j in range(n):
                if can_reach(robots[i], holes[j], s):
                    g[f'robot{i}'][f'hole{j}'] += 1
                else:
                    g[f'robot{i}'][f'hole{j}'] = 0

        flow = FordFulkerson(g, 'start', 'sink', m)
        max_flow += flow
        if max_flow >= m:
            if s == 5:
                print(f"In {5} seconds {max_flow} robot(s) can escape")
                print(f"In {10} seconds {max_flow} robot(s) can escape")
                print(f"In {20} seconds {max_flow} robot(s) can escape")
                break
            elif s==10:
                print(f"In {10} seconds {max_flow} robot(s) can escape")
                print(f"In {20} seconds {max_flow} robot(s) can escape")
                break
            else:
               print(f"In {s} seconds {max_flow} robot(s) can escape") 
               break
        else:
            print(f"In {s} seconds {max_flow} robot(s) can escape")
        s *= 2
    print()
