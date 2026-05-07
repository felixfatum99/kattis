n = int(input())

d = set()
liste = []
for _ in range(n):
    apps = input().split()
    for i in range(1, int(apps[0])+1, 1):
        if apps[i] not in d:
            d.add(apps[i])
            liste.append(apps[i])
            break
print(" ".join(liste))
