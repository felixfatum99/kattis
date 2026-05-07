import sys

x, y = 0, 0
d = {}
d[(0, 0)] = 'S'

min_x = max_x = 0
min_y = max_y = 0

for line in sys.stdin:
    c = line.replace("\n", "")

    if c == 'down':
        y+=1
    if c == 'up':
        y-=1
    if c == 'left':
        x-=1
    if c == 'right':
        x+=1
    
    if (x, y) not in d:
        d[(x, y)] =  '*'
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    min_x = min(min_x, x)
    min_y = min(min_y, y)

d[(x, y)] = 'E'

for j in range(min_y-1, max_y+2, 1):
    for i in range(min_x-1, max_x+2, 1):
        if (i, j) in d:
            print(d[(i, j)],end="")
        else:
            print("#" if i == min_x-1 or i == max_x+1 or j == min_y-1 or j == max_y+1 else " " , end="")
    print()
    