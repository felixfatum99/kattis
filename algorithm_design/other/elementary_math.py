#Implemented code with inspiration GeeksforGeeks
from collections import defaultdict, deque
#import random
import sys
#import time

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

    paths = dict()
    for k in g['sink'].keys():
        for v in g[k].keys():
            if g[k][v] == 1:
                if v in paths.keys():
                    paths[v].append(k)
                else:
                    paths[v] = [k]

    return max_flow, paths

def main():
    n = int(input())
    #t = time.time()
    g = defaultdict(lambda: defaultdict(int))
    correct_order = []
    data = sys.stdin.read().splitlines()

    for line in data:
        a, b = map(int, line.split())
        #a, b = (random.randint(-1000000, 1000000), random.randint(-1000000, 1000000))
        correct_order.append((a, b))
        
        prod, diff, summ = a * b, a - b, a + b
        if g['start'][(a, b)] >= 3:
            print("impossible")
            exit()

        g['start'][(a, b)] += 1
        g[(a, b)][prod] += 1
        g[(a, b)][diff] += 1
        g[(a, b)][summ] += 1
        g[prod]['sink'] = 1
        g[diff]['sink'] = 1
        g[summ]['sink'] = 1
        
        g['sink'][prod] =  0
        g['sink'][diff] =  0
        g['sink'][summ] = 0

    count, paths = FordFulkerson(g, 'start', 'sink')
    if count >= n:
        for p in correct_order:
            a = p[0]
            b = p[1]
            res = paths[p].pop()
            if a + b == res:
                print(f"{a} + {b} = {res}")
            elif a * b == res:
                print(f"{a} * {b} = {res}")
            elif a - b == res:
                print(f"{a} - {b} = {res}")
        #print("done in", time.time()-t)
    else:
        print("impossible")

main()