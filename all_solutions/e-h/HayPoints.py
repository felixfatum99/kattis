import sys

m, n = map(int, input().split())
d = {}

for _ in range(m):
    k, v = input().split()
    d[k] = int(v)

for _ in range(n):
    res = 0
    try:
        while True:
            line = input().strip()
            if line == ".":
                print(res)
                break
            words = line.split()
            for word in words:
                res += d.get(word, 0)
    except EOFError:
        break
