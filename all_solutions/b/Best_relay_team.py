#https://open.kattis.com/problems/bestrelayteam
n = int(input())
l = []
for i in range(n):
    r, s, f = map(str, input().split(" "))
    s = float(s)
    f = float(f)
    l.append((r, s, f))
l.sort(key=lambda p: p[1])  
ll = sorted(l, key=lambda p: p[2])

best_time = float("inf")
best_runners = []

for r in l:
    temp_runners = []
    temp = 0
    temp_runners.append(r)
    temp+=r[1]
    x = 0
    while len(temp_runners)<4:
        if ll[x] not in temp_runners:
            temp_runners.append(ll[x])
            temp+=ll[x][2]
        x+=1
    if temp < best_time:
        best_time = temp
        best_runners = temp_runners

print(best_time)
for r in best_runners:
    print(r[0])