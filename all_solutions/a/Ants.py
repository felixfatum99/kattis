#https://open.kattis.com/problems/ants
import sys

def compute(all_ants, l, n):
    all_ants.sort()
    lowest = 0
    highest = 0

    for pos in all_ants:
        highest = max(highest, max(l-pos, pos))
        lowest = max(lowest, min(pos, l-pos))

    print(lowest, highest)


c = int(input())

for i in range(c):
    l, n = map(int, input().split())
    ants = []
    while len(ants) < n:
        ants += ([int(x) for x in input().split()])

    compute(ants, l, n)