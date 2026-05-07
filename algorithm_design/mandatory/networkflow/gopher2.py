import math
import sys
#Implemented code with inspiration GeeksforGeeks

def BFS(g, r, s, t, p):
    v = [False]*(r)
    q = []
    q.append(s)
    v[s] = True

    while q:
        u = q.pop(0)
        for i, val in enumerate(g[u]):
            if v[i] == False and val > 0:
                q.append(i)
                v[i] = True
                p[i] = u
                if i == t:
                    return True
    return False
             
def FF(g, r, src, z):
    p = [-1]*(r)
    mf = 0 
    while BFS(g, r, src, z, p) :
        pf = float("Inf")
        s = z
        while(s !=  src):
            pf = min (pf, g[p[s]][s])
            s = p[s]

        mf +=  pf

        v = z
        while(v !=  src):
            u = p[v]
            g[u][v] -= pf
            g[v][u] += pf
            v = p[v]
    return mf

def can_reach(c1, c2, s, v):
    dist = math.dist(c1, c2)
    if s*v >= dist:
        return True
    else:
        return False

while True:
    l = sys.stdin.readline()
    if l == '':
        break

    n, m, s, v = map(int, l.split(" "))
    
    gopher = []
    holes = []

    for i in range(n):
        x, y = map(float, input().split(" "))
        gopher.append((x, y))
    
    for j in range(m):
        x, y = map(float, input().split(" "))
        holes.append((x, y))
    
    g = [[0 for _ in range(n+m+2)] for _ in range(n+m+2)]
    
    for i in range(n):
        g[0][i+1] = 1
    
    for i in range(n+1, n+m+1):
        g[i][n+m+1] = 1

    for i in range(n):
        for j in range(m):
            if can_reach(gopher[i], holes[j], s, v):
                g[i+1][n+j+1] += 1

    print(n-FF(g, len(g), 0, n+m+1))
