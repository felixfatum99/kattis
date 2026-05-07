def dt(str1, str2):
    def lcs(X, Y):
        m, n = len(X), len(Y)
        dp = [[""] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if X[i - 1] == Y[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + X[i - 1]
                else:
                    dp[i][j] = dp[i - 1][j] if len(dp[i - 1][j]) > len(dp[i][j - 1]) else dp[i][j - 1]
        return dp[m][n]

    s = lcs(str1, str2)
    i, j = 0, 0
    result = []

    for c in s:
        while i < len(str1) and str1[i] != c:
            result.append(str1[i])
            i += 1
        while j < len(str2) and str2[j] != c:
            result.append(str2[j])
            j += 1
        result.append(c)
        i += 1
        j += 1

    result.append(str1[i:])
    result.append(str2[j:])

    return ''.join(result)

str1 = input()
str2 = input()
result = dt(str1, str2)
print(result)
