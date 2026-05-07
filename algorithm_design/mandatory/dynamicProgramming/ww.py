def ww(p):
    t = 1000
    ms = 2000  
    r = 0
    md = float('inf')
    
    dp = [False] * (ms + 1)
    dp[0] = True  
    
    for w in p:
        for j in range(ms, w - 1, -1):
            dp[j] = dp[j] or dp[j - w]
            if dp[j]:
                d = abs(j - t)
                if d < md or (d == md and j > r):
                    r = j
                    md = d

    return r


n = int(input())
p = []
for i in range(n):
    p.append(int(input()))
print(ww(p))
