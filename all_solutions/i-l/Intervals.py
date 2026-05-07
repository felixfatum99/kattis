a, b = map(int, input().split())
hours = [0 for _ in range(25)]
for i in range(a):
    s, t = map(int, input().split())
    for k in range(s+1, t+1, 1):
        hours[k] += 1

sum = 0
for hour in hours:
    if hour >= b:
        sum+= 1
print(sum)