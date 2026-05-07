n = int(input())
l = [int(x) for x in input().split()]
l.sort(reverse=True)

day = 2
highest = 0
for i in range(n):
    highest = max(l[i]+day, highest)
    day += 1

print(highest)