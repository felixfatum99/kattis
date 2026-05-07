import heapq

def p():
    i = int(input())
    p = []
    h = []

    for x in range(i):
        pp = [int(x) for x in input().split(" ", -1)]
        p.append((pp[0], pp[1]))
    
    p.sort()

    for d, m in p:
        if len(h) < d:
            heapq.heappush(h, m)
        else:
            if h and h[0] < m:
                heapq.heappop(h)
                heapq.heappush(h, m)
    
    print(sum(h))
p()