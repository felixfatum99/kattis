n = int(input())

count = 0
for i in range(n):
    p, d, a = map(str, input().split())
    if d == "IN":
        count += int(a)
    else:
        count -= int(a)

print(count if count > 0 else "NO STRAGGLERS")