from collections import deque
N, M = map(int, input().split())

def mark_sea(map):
    rows = len(map)
    cols = len(map[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    queue = deque()
    queue.append((0, 0))

    while queue:
        current_pos = queue.pop()
        visited[current_pos[0]][current_pos[1]] = True
        map[current_pos[0]][current_pos[1]] = "S"

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = current_pos[0] + dr, current_pos[1] + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and map[nr][nc] == "0":
                queue.append((nr, nc))

def count_length(map):
    count = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if map[i][j] == "1":
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = i + dr, j + dc
                    if map[nr][nc] == "S":
                        count += 1
    return count
                        
map = []
map.append(["0"] * (M+2))
for _ in range(N):
    row = input()
    row = "0"+row+"0"
    map.append(list(row))
map.append(["0"] * (M+2))

mark_sea(map)
print(count_length(map))