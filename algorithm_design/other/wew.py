n = int(input())
m = [None]*(n+1)
m[0] = 0
intervals = []

for i in range(n):
    s, f, w = map(int, input().split(" "))
    intervals.append((s, f, w))

intervals.sort(key=lambda p: p[1])
p=[0]*(n+1)
p[1] = 0
for j in range(1, n, 1):
    for i in range(j-1, -1, -1):
        if intervals[i][1]<=intervals[j][0]:
            p[j+1]=i+1
            break
print(p)
for j in range(1, n+1, 1):
    m[j] = max((intervals[j-1][2]+m[p[j]]), m[j-1])

print(m[n])