from collections import deque

def bfs(g, start, n):
    q = deque()
    q.append(start)

    visited = set()
    visited.add(start)
    
    parent = {start: None}

    moves = {(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)}
    while q:
        current = q.popleft()

        if current == (0, 0):
            return True, parent, current

        for move in moves:
            neighbor = (current[0]+move[0], current[1]+move[1])
            if neighbor not in visited and 0 <= neighbor[0] <= n-1 and 0 <= neighbor[1] <= n-1 and g[neighbor[0]][neighbor[1]] != "#":
                q.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current

    return False, parent, current
    

rc = int(input())
board = []
start = None

for i in range(rc):
    row = list(input())
    board.append(row)

    if "K" in row:
        start = (i, row.index("K"))


res = bfs(board, start, rc)

if res[0]:
    current = res[2]
    i = 0

    while True:        
        current = res[1][current]
        if current == None:
            print(i)
            break
        i += 1
else:
    print(-1)