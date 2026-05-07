def c():
    t = int(input())
    p = [int(x) for x in input().split(" ", -1)]
    p.sort()
    s = 0
    while len(p) > 2:
        p.pop()
        p.pop()
        s += p.pop()
    print(s)

c()