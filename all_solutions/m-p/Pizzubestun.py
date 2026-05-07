n = int(input())
prices = []
output = 0

for x in range(n):
    pizza = input().split(" ")
    prices.append(int(pizza[1]))

prices.sort(reverse=True)

length = len(prices)
if len(prices) % 2 != 0:
    output+=prices[len(prices)-1]
    length-=1

for i in range(0, length, 2):
    output+=prices[i]

print(output)