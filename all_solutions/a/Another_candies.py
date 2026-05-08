#https://open.kattis.com/problems/anothercandies
import sys

data = sys.stdin.read().split()
t = int(data[0])
idx = 1

answers = []

for _ in range(t):
    n = int(data[idx])
    idx += 1

    total = 0
    for _ in range(n):
        total = (total + int(data[idx])) % n
        idx += 1

    answers.append("YES" if total == 0 else "NO")

print("\n".join(answers))