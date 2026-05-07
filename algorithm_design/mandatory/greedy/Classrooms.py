import bisect

def c():
    n, k = map(int, input().split())
    t = [tuple(map(int, input().split())) for _ in range(n)]
    t.sort(key=lambda x: (x[1], x[0])) 
    r = []
    e = 0
    for s, f in t:
        p = bisect.bisect_right(r, s - 1)
        if p > 0: 
            r.pop(p - 1) 
        if len(r) < k:
            bisect.insort(r, f) 
            e += 1
    print(e)
c()
    