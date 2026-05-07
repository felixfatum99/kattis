import sys

def knapSack(W, wt, val, n):
    dp = [0 for i in range(W+1)]
    
    for i in range(1, n+1):
        for w in range(W, 0, -1):
            if wt[i-1] <= w:
                if not dp[w] > dp[w-wt[i-1]]+val[i-1]:
                    dp[w] = dp[w-wt[i-1]]+val[i-1]
    

while True:
    l = sys.stdin.readline()
    if l == '':
        break
    C, n = map(int, l.split(" "))
    value = []
    weight = []

    for i in range(n):
        v, w = map(int, sys.stdin.readline().split(" "))
        value.append(v)
        weight.append(w)

    knapSack(C, weight, value, n)
