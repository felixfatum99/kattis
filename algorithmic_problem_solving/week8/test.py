from collections import defaultdict

t = int(input())
for _ in range(t):
    input()
    n = int(input())
    arr = list(map(int, input().split()))

    target = 47

    prefix = 0
    count = 0
    freq = defaultdict(int)
    freq[0] = 1

    for x in arr:
        prefix += x
        count += freq[prefix - target]
        freq[prefix] += 1

    print(count)