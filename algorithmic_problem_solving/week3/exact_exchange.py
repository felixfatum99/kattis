n = int(input())
for i in range(n):
    target = int(input())
    money = int(input())
    m = []
    for j in range(money):
        b = int(input())
        m.append(b)
    m.sort()
    dp = [(False, 0)]*10001
    dp[0] = (True, 0)
    for bill in m:
        for i in range(10000-bill, -1, -1):
            if dp[i][0]:
                if not dp[i + bill][0] or dp[i + bill][1] > dp[i][1] + 1:
                    dp[i+bill] = (True, dp[i][1]+1)
    for i in range(len(dp)):
        if dp[i][0] and i >= target:
            print(i, dp[i][1])
            break