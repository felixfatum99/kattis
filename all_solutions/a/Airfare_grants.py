#https://open.kattis.com/problems/airfaregrants
n = int(input())

prices = []
for _ in range(n):
    prices.append(int(input()))
prices.sort()
print(max(int(prices[0]-(prices[n-1]/2)),0))