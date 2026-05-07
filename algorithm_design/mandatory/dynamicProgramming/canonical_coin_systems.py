inf = float("inf")

n = int(input())
a = list(map(int, input().split()))

a.sort() 
m = a[len(a)-2]+a[len(a)-1]

dp = [inf] * m
g = [inf] * m

dp[0] = 0
g[0] = 0

x = 0
w = True

for i in range(1, m):
    while x < n - 1 and a[x + 1] <= i:
        x += 1
    
    g[i] = g[i - a[x]] + 1
    
    for j in range(n):
        if a[j] <= i:
            dp[i] = min(dp[i], dp[i - a[j]] + 1)

    if g[i] != dp[i]:
        w = False
        break

if w:
    print("canonical")
else:
    print("non-canonical")

