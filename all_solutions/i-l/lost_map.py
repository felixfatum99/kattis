import sys

def primMST(graph, V):
    key = [sys.maxsize] * V
    parent = [None] * V  
    key[0] = 0
    mstSet = [False] * V

    parent[0] = -1 

    for cout in range(V):
        min = sys.maxsize
        for v in range(V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        u = min_index

        mstSet[u] = True

        for v in range(V):
            if graph[u][v] > 0 and mstSet[v] == False \
            and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u

    for i in range(1, V):
        print(parent[i]+1, i+1)


n = int(input())
graph = [[int(x) for x in input().split()] for _ in range(n)]

primMST(graph, n)