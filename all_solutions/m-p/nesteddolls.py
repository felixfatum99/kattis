import sys
from bisect import bisect_left, insort

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    m = int(input())
    inp = list(map(int, input().split()))

    dolls = [(inp[i], inp[i + 1]) for i in range(0, 2 * m, 2)]
    dolls.sort(key=lambda x: (x[0], -x[1]))

    tops = []

    for _, h in dolls:
        idx = bisect_left(tops, h) - 1

        if idx >= 0:
            tops.pop(idx)
        insort(tops, h)

    print(len(tops))
