from collections import defaultdict

a, b = map(int, input().split())
graph = []


for i in range(a):
    line = input()
    temp = []
    for j in range(b):
        temp.append(line[j])
    graph.append(temp)

def create_land(y, x):
    s_y, s_x = y, x
    global graph
    if x-1 >= 0:
            x, y = x-1, y
            if graph[x][y] == "C":
                graph[x][y] = "L"
                create_land(x, y)
    if x+1 <= b-1:
            x = s_x
            y = s_y
            x, y = x+1, y
            if graph[x][y] == "C":
                graph[x][y] = "L"
                create_land(x, y)
    if y-1 >= 0:
        x = s_x
        y = s_y
        x, y = x, y-1
        if graph[x][y] == "C":
            graph[x][y] = "L"
            create_land(x, y)

    if y+1 <= a-1:
        x = s_x
        y = s_y
        x, y = x, y+1
        if graph[x][y] == "C":
            graph[x][y] = "L"
            create_land(x, y)

for i in range(a):
    for j in range(b):
        if graph[i][j] == "L":
            create_land(i, j)

for i in range(a):
    for j in range(b):
        if j == b-1:
            print(graph[i][j])
        else:
            print(graph[i][j], end="")
    
