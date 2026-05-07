from collections import defaultdict, deque
import sys

def bfs(g, src, dest, parent, mincap=0):
    visited = {i: False for i in g.keys()}
    queue = deque([src])
    visited[src] = True
    parent[src] = src

    while queue:
        u = queue.popleft()
        for v in g[u]:
            if not visited[v] and g[u][v] > mincap:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == dest:
                    return True
    return False

def ford_fulkerson(g, src, dest):
    max_flow = 0
    parent = {i: -1 for i in g.keys()}
    max_capacity = max(max(d.values()) for d in g.values() if d)

    mincap = max_capacity
    while True:
        if not bfs(g, src, dest, parent, mincap):
            if mincap > 0:
                mincap //= 2
                continue
            else:
                break
        
        path_flow = float("Inf")
        v = dest
        while v != src:
            u = parent[v]
            path_flow = min(path_flow, g[u][v])
            v = parent[v]

        max_flow += path_flow
        v = dest
        while v != src:
            u = parent[v]
            g[u][v] -= path_flow
            g[v][u] += path_flow
            v = parent[v]

    return max_flow

def main():
    n = int(input())
    g = defaultdict(lambda: defaultdict(int))
    correct_order = []
    
    for _ in range(n):
        a, b = map(int, input().split())
        correct_order.append((a, b))

        prod, diff, summ = a * b, a - b, a + b

        g["start"][(a, b)] += 1
        g[(a, b)][prod] += 1
        g[(a, b)][diff] += 1
        g[(a, b)][summ] += 1

        g[prod]["sink"] = 1
        g[diff]["sink"] = 1
        g[summ]["sink"] = 1
        g['sink'][prod] =  0
        g['sink'][diff] =  0
        g['sink'][summ] = 0
        

    max_flow = ford_fulkerson(g, "start", "sink")
    
    if max_flow != n:
        print("impossible")
        return

    for ab in correct_order:
        a, b = ab[0], ab[1]
        res = [x for x in g['sink'].keys() if g['sink'][x]>0 and g[x][ab] == 1]
        res = res[0]
        g['sink'][res] = 0
        if a + b == res:
            print(f"{a} + {b} = {a + b}")
        elif a - b == res:
            print(f"{a} - {b} = {a - b}")
        elif a * b == res:
            print(f"{a} * {b} = {a * b}")

main()
