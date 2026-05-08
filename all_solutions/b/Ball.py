#https://open.kattis.com/problems/ball
n = int(input())
d = dict()
for i in range(n+1):
    d[str(i)] = 0

for _ in range(int((n/2))+1):
    a, b = map(str, input().split())
    d[a] += 1
    d[b] += 1

output = ""
for i in range(1, n+1):
    if d[str(i)] > 1:
        output+= str(i)+" "

print(output)