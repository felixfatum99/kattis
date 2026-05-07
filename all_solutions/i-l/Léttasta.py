n = int(input())
m = int(input())

d = {}
problems = [name for name in input()]
for i in range(n):
    d[problems[i]] = 0

for i in range(m):
    scores = [int(x) for x in input()]
    for j in range(n):
        d[problems[j]] += scores[j]

print(d)