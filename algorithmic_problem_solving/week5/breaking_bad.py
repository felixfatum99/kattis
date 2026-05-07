from collections import deque

def isBipartite(V, adj):
    color = [-1] * V  
    
    for i in range(V):
        if color[i] == -1:
            color[i] = 0	
            q = deque([i])

            while q:
                u = q.popleft()

                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        return False 
    return color
                    
n = int(input())

graph = [[] for _ in range(n)]
dic = {}
inv_dic = {}

for j in range(n):
    name = input()
    dic[name] = j
    inv_dic[j] = name
    
m = int(input())

for i in range(m):
    a, b = input().split(" ")
    graph[dic[a]].append(dic[b])
    graph[dic[b]].append(dic[a])

res = isBipartite(n, graph)

if res == False:
    print("impossible")
else:
    for i, j in enumerate(res):
        if j == 0:
            print(inv_dic[i], end=" ")
    print()

    for i, j in enumerate(res):
        if j == 1:
            print(inv_dic[i], end=" ")
