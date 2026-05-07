import bisect

n = int(input())

prices = {}
arr = []

for _ in range(n):
    name, guess = map(str, input().split())
    guess = int(guess)
    prices[guess] = name
    arr.append(guess)

arr.sort()

t = int(input())

for _ in range(t):
    p = int(input())
    index = bisect.bisect(arr, p)
    if index == 0:
        print(":(")
    else:
        print(prices[arr[index-1]])
