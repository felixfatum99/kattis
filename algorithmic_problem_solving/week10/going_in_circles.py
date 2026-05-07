from collections import deque
import random

terminate = False
l = 10

s = input()
if s == '1':
    print("? flip", flush=True)
    input()

for _ in range(l):
    print("? right", flush=True)
    ans = input()
    if ans == '1':
        print("? flip", flush=True)
        input()

for i in range(l):
    print("? left", flush=True)
    ans = input()
    if ans == '1':
        print("!", i, flush=True)
        terminate = True
        break
    else:
        print("? flip", flush=True)
        input()

if not terminate:
    seq = [str(random.randint(0, 1)) for _ in range(l)]
    for j in range(l):
        print("? right", flush=True)
        ans = input()
        if seq[j] != ans:
            print("? flip", flush=True)
            input()

    q = deque()
    answer = l

    for _ in range(l):
        print("? right", flush=True)
        q.append(input())

    while list(q) != seq:
        q.popleft()
        print("? right", flush=True)
        q.append(input())
        answer += 1

    print("!", answer, flush=True)
