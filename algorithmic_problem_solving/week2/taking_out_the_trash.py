from collections import deque 
import sys

input = sys.stdin.buffer.readline

N, M = map(int, input().split())

trash = sorted([int(x) for x in input().split()], reverse=True)
q = deque(trash)

walks = 0

while q:
    left_hand = q.popleft()
    walks += 1

    if not q:
        break

    right_hand = q.pop()

    if left_hand + right_hand > M:
        q.append(right_hand)

print(walks)