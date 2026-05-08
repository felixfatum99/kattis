import sys
input = sys.stdin.buffer.readline

n = int(input())
d = {}

for _ in range(n):
    c, y = input().split()
    if c not in d:
        d[c] = []
    d[c].append(int(y))

for k in d:
    d[k].sort()
    
t = int(input())

for i in range(t):
    c, k = input().split()
    print(d[c][int(k)-1])