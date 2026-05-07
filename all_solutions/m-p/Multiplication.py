n = int(input())

prod = 1

for _ in range(n):
    prod *= int(input())

print(prod%((10**9)+7))