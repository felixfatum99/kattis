a, b = map(int, input().split())

arr = [0 for i in range(a)]

for i in range(b):
    x, y = map(int, input().split())
    arr[y-1]+=1

min = float('inf')
for i in range(a):
    if arr[i] < min:
        min = arr[i]

print(min)
