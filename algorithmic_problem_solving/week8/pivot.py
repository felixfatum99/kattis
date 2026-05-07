a = int(input())
b = [int(x) for x in input().split()]
l = [True] * a
h = [True] * a

current_highest = b[0]
current_lowest = b[a-1]

for i in range(0, a, 1):
    if b[i] < current_highest:
        l[i] = False
    if b[a-i-1] > current_lowest:
        h[a-i-1] = False
    current_highest = max(current_highest, b[i])
    current_lowest = min(current_lowest, b[a-i-1])

sum = 0
for i in range(a):
    if l[i] and h[i]:
        sum+=1

print(sum)