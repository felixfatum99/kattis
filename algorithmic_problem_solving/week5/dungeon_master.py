from collections import deque

def neighbours(node, grid, L, R, C):
    z, x, y = node
    targets = {'.', 'E', 'S'}
    res = []
    for dz, dx, dy in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
        nz, nx, ny = z+dz, x+dx, y+dy
        if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C and grid[nz][nx][ny] in targets:
            res.append((nz, nx, ny))
    return res

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break

    grid = []
    start = None

    for z in range(L):
        level = []
        for x in range(R):
            row = list(input().rstrip())
            if 'S' in row:
                start = (z, x, row.index('S'))
            level.append(row)
        input()  
        grid.append(level)

    q = deque([(start, 0)])  
    visited = set([start])
    escaped = False
    ans = None

    while q:
        node, dist = q.popleft()
        z, x, y = node

        if grid[z][x][y] == 'E':
            escaped = True
            ans = dist
            break

        for nb in neighbours(node, grid, L, R, C):
            if nb not in visited:
                visited.add(nb)
                q.append((nb, dist + 1))

    if escaped:
        print(f"Escaped in",ans,"minute(s).")
    else:
        print("Trapped!")