n = int(input())

hit = 0
m = 1
score = 0
for _ in range(n):
    note = int(input())
    if note == 0:
        m = max(1, m/2)
        hit = 0
    else:
        if hit+1 == m*2:
            m = min(m*2, 8)
            hit = -1
        score += m*note
        hit += 1

print(int(score))