from collections import defaultdict, deque

def BFS(g, s, t, max_capacity):
    visited = set([s])
    q = deque([s])
    parent = {s: None}

    while q:
        u = q.popleft()
        for v, cap in g[u].items():
            if v not in visited and cap > max_capacity:
                visited.add(v)
                parent[v] = u
                if v == t:
                    return True, parent
                q.append(v)
    return False, parent

def FordFulkerson(res, source, sink):
    max_flow = 0

    max_capacity = 100001

    while True:
        found_path, parent = BFS(res, source, sink, max_capacity)
        if not found_path:
            if max_capacity > 0:
                max_capacity = max_capacity // 2
                continue
            else:
                return max_flow

        path_flow = float("inf")
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, res[u][v])
            v = u

        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            res[u][v] -= path_flow
            res[v][u] += path_flow
            v = u

def build_graph(grid, x, y):
    INF = 100000
    rows, cols = len(grid), len(grid[0])
    graph = defaultdict(lambda: defaultdict(int))

    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    S = "S"

    def outer(r,c):
        return r == 0 or r == rows-1 or c == 0 or c == cols-1

    for r in range(rows):
        for c in range(cols):

            if grid[r][c] == 0:
                continue

            node_in = r*cols+c
            node_out = r*cols+c+INF

            graph[node_in][node_out] = grid[r][c]

            if outer(r,c):
                graph[S][node_in] = INF

            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] != 0:

                    neighbor_in = nr*cols+nc
                    graph[node_out][neighbor_in] = INF

    castle = (x*cols+y)+INF
    graph[castle]["T"] = grid[x][y]
    graph["T"]
    return graph


import sys
input = sys.stdin.readline

grid = []
R, C = map(int, input().split())

for i in range(R):
    column = [int(x) for x in input().split()]
    grid.append(column)

cx, xy = map(int, input().split())

g = build_graph(grid, cx, xy)
maxflow = FordFulkerson(g, "S", "T")
print(maxflow)
