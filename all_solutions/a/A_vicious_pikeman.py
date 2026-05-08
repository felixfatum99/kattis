#https://open.kattis.com/problems/pikemaneasy
n, m = map(int, input().split())
A, B, C, t0 = map(int, input().split())

times = [t0]
for i in range(1, n):
    times.append(((A * times[i-1] + B) % C) + 1)

times.sort()

problems = 0
penalty = 0
elapsed = 0 

for t in times:
    if elapsed + t > m:
        break
    elapsed += t
    problems += 1
    penalty = (penalty + elapsed) % 1_000_000_007

print(problems, penalty)