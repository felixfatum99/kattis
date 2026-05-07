# used this https://www.geeksforgeeks.org/dsa/unbounded-knapsack-repetition-items-allowed/ for solving if only one solution

import sys 

input = sys.stdin.buffer.readline

def dp(items, order):
    dp = [[] for _ in range(order+1)]
    dp[0].append(1)

    for item in items:
        for i in range(order+1):
            if len(dp[i]) > 0 and i+item < (order+1):
                if len(dp[i+item]) > 0:
                    dp[i+item][0]+=dp[i][0]
                else:
                    dp[i+item] += dp[i] + [item]
                    dp[i+item][0] = dp[i][0]
    return dp

N = int(input())

items = [int(x) for x in input().split()]

O = int(input())

orders = [int(x) for x in input().split()]
max_val = max(orders)
unique = dp(items, max_val)

for order in orders:
    if len(unique[order]) == 0:
        print("Impossible")
    elif unique[order][0] > 1:
        print("Ambiguous")
    else:
        for i, val in enumerate(unique[order]):
            if i != 0:
                print(items.index(val)+1, end=" ")
