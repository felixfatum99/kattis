#https://open.kattis.com/problems/akcija
n = int(input())

prices = []
for _ in range(n):
    prices.append(int(input()))

prices.sort(reverse=True)
sum = 0
for i in range(len(prices)):
    if (i+1) % 3 != 0:
        sum+=prices[i]
print(sum)
