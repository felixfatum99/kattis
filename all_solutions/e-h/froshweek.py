count = 0
n = int(input())
s = []

for _ in range(n):
    s.append(int(input()))

def rec(l):
    if len(l) < 2:
        return l, 0
    m = len(l) // 2
    v, cv = rec(l[:m])
    h, ch = rec(l[m:])
    r = []
    i,j=0,0
    c = 0
    while i < len(v) and j < len(h):
        if v[i] <= h[j]:
            r.append(v[i])
            i += 1
        else:
            r.append(h[j])
            c += len(v) - i
            j += 1

    r += v[i:]
    r += h[j:]
    return r, c+cv+ch

print(rec(s)[1])