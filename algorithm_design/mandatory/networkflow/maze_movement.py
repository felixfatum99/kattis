import math
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

n = int(input())
v = []

for i in range(n):
    v.append(int(input()))

v.sort()

g = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(i, n):
        if i == j:
            continue
        else:
            if math.gcd(v[i], v[j]) != 1:
                x = math.gcd(v[i], v[j])
                g[i][j] = x
                g[j][i] = x

print(FF(g, len(g), 0, n-1))