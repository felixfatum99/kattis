def walls_covered(p, c, r):
    s = ''
    rx, ry = p
    for i, P in enumerate(c):
        dx = rx - P[0]
        dy = ry - P[1]
        if dx*dx + dy*dy <= r*r:
            s+='1'
        else:
            s+='0'
    return int(s, 2)

def dp(masks):
    dp = [float('inf')] * 16
    dp[0] = 0
    mask = int('0000', 2)
    for m in masks:                                
        for mask in range(16):       
            if dp[mask] < float('inf'):
                newMask = mask | m
                dp[newMask] = min(dp[newMask], dp[mask] + 1)

    return dp[15] if dp[15] < float('inf') else "Impossible"



l, w, n, r = map(int, input().split())
cranes = [(-l/2, 0),(l/2, 0), (0, -w/2), (0, w/2)]
masks = []

for i in range(n):
    x, y = map(int, input().split())
    masks.append(walls_covered((x, y), cranes, r))

print(dp(masks))