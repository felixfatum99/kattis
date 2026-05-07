def wc():
    t = int(input())

    for i in range(t):
        n = int(input())
        
        p = []
        for j in range(n):
            inf = [float(x) for x in input().split(" ")]
            p.append(sum(inf[1:]))

        output = 0
        cwt = 0
        p.sort()
        for i in range(len(p)):
            output += (cwt+p[i])
            cwt += p[i]
        print(output/len(p))

wc()