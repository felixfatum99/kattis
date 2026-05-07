t = int(input())
list = []
m = 0


for i in range(t):
    n = int(input())
    list.append(n)
    if n > m:
        m = n

dp = [[[0 for k in range((m+1))]for j in range(2*m+1)]for i in range(2*m+1)]
dp[m][m][0] = 1

for i in range(1, m, 1):
    for j in range(2*m):
        for k in range(2*m):
            if k>0:
                dp[j][k][i] += dp[j][k-1][i-1]
            if j > 0:
                dp[j][k][i] += dp[j-1][k][i-1]
            if j > 0 and k > 0:
                dp[j][k][i] += dp[j-1][k-1][i-1]
            if j < 2*m+1:
                dp[j][k][i] += dp[j+1][k][i-1]
            if k < 2*m+1:
                dp[j][k][i] += dp[j][k+1][i-1]
            if j < 2*m+1 and k < 2*m+1:
                dp[j][k][i] += dp[j+1][k+1][i-1]
                
for x in list:
    print(dp[m][m][x])