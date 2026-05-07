import sys
from bisect import bisect_left

def LIS(a, l):
    dp = []
    p = [-1] * l  
    P = [-1] * l 
    li = 0 

    for i in range(l):
        x = bisect_left(dp, a[i])

        if x < len(dp):
            dp[x] = a[i]
        else:
            dp.append(a[i])
        
        P[x] = i
        if x > 0:
            p[i] = P[x - 1]
        
        if x == len(dp) - 1:
            li = i

    result = []
    while li != -1:
        result.append(li)
        li = p[li]
    
    result.reverse()
    
    return len(dp), ' '.join(map(str, result))

while True:
    l1 = sys.stdin.readline().strip()
    if l1 == '':
        break
    else:
        l2 = [int(x) for x in input().split()]
        n, m = LIS(l2, len(l2))
        print(n)
        if n == 1:
            print(int(l1) - 1)
        else:
            print(m)
