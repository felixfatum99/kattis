from collections import deque
from collections import defaultdict

def r():
    n = [int(x) for x in input().split(" ", -1)]
    p = []
    r = dict()
    for i in range(n[0]+n[2]):
        if i < n[0]:
            l = [x for x in input().split(" ", -1)]
            pr = ps(l[0], l[1:])
            p.append(pr)
        else:
            l = [x for x in input().split(" ", -1)]
            rj = a(l[0], l[1:])
            r[l[0]]= rj      

    gs(p, r, n[1])

def gs(P, R, t):
    s = defaultdict(dict)
    u = deque(P)

    while u:
        p = u.popleft()
        r = R[p.f.pop()]

        if r.u:
            s[p.n][r.n]=r.n
            r.cp = p
            r.u = False
            p.count += 1

            if p.count < t:
                u.appendleft(p)
            elif p.count == t:
                p.u = False
            
        elif not r.u:
            if r.f[r.cp.n] > r.f[p.n]:
                if not r.cp.u:
                    u.appendleft(r.cp) 
                r.cp.u = True
                r.cp.count -= 1
                del s[r.cp.n][r.n]
                s[p.n][r.n] = r.n
                p.count += 1
                if p.count < t:
                    u.appendleft(p)
                elif p.count == t:
                    p.u = False
                r.cp = p
            else:
                if len(p.f) > 0:
                    u.appendleft(p)

    for i in s:
        x = " ".join(s[i].values())
        print(i, x)

class ps:
    def __init__(self, n, l):
        self.f = l
        self.f.reverse()
        self.n = n
        self.u = True
        self.count = 0

class a:
    def __init__(self, n, l):
        self.n = n
        self.f = self.td(l)
        self.u = True
        self.cp = ""

    def td(self, l: list):
        d = dict()
        for i in range(len(l)):
            d[l[i]] = i+1
        return d

r()