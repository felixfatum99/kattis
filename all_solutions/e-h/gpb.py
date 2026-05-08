import sys
import bisect

input = sys.stdin.buffer.readline

n = int(input())
l = []

for _ in range(n):
    c, y = input().split()
    l.append((c, int(y)))

l.sort(key=lambda p: (p[0], p[1]))

q = int(input())
out = []

for _ in range(q):
    c, k = input().split()
    out.append(str(l[bisect.bisect_left(l, (c, -1)) + int(k) - 1][1]))

sys.stdout.write("\n".join(out))