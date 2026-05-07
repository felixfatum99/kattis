n = int(input())

lasers = []
for _ in range(n):
    x, y, m, name = map(str, input().split())
    x = float(x)
    y = float(y)
    m = float(m)
    if m == 0:
        if x == 0:
            lasers.append((x, name))
    else:
        b = y -(m*x)
        x_intersect = -b/m  
        if x_intersect > x:
            lasers.append((x_intersect, name))

lasers =  sorted(lasers, key=lambda x: x[0])

for l in lasers:
    print(l[1])
