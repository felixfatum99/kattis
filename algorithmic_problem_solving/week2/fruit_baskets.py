f = int(input())
fruits = list(map(int, input().split()))

MAX_SUM = sum(fruits)
dp = [0] * (MAX_SUM + 1)
dp[0] = 1

for fruit in fruits:
    for w in range(MAX_SUM, fruit - 1, -1):
        dp[w] += dp[w - fruit]

ans = 0
for w in range(200, MAX_SUM + 1):
    ans += w * dp[w]

print(ans)