#https://open.kattis.com/problems/buildinfences
min_x, max_x = float('inf'), float('-inf')
min_y, max_y = float('inf'), float('-inf')
for i in range(int(input())):
    x, y = map(int, input().split())
    min_x = min(x-1, min_x)
    max_x = max(x+1, max_x)
    min_y = min(y-1, min_y)
    max_y = max(y+1, max_y)

print((max_x-min_x)*2+(max_y-min_y)*2)


