import math
import sys

def wg():
    for line in sys.stdin:
        n, l, w = map(int, line.split(" "))
        sprinklers = [tuple(map(int, input().split())) for _ in range(n)]
        
        c = []
        half_width = w / 2.0
        
        for x, r in sprinklers:
            if r > half_width:
                p = math.sqrt(r**2 - half_width**2)
                left = max(0, x - p)
                right = min(l, x + p)
                c.append((left, right))

        c.sort()

        sum = 0
        lc = 0
        i = 0
        
        while lc < l:
            fc = lc
            while i < len(c) and c[i][0] <= lc:
                fc = max(fc, c[i][1])
                i += 1
            
            if fc == lc:
                sum = -1
                break
            
            lc = fc
            sum += 1
        
        print(sum)
wg()
