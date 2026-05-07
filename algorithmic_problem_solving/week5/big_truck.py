import sys 
import heapq

def insert(a, b, d, graph):
    if a in graph:
        graph[a].append((b, d))
    else:
        graph[a] = [(b, d)]
    
    if b in graph:
        graph[b].append((a, d))
    else:
        graph[b] = [(a, d)]

n = int(input())

pick_up = [0]+[int(c) for c in input().split()]

m = int(input())

graph = {}

for i in range(m):
    a, b, d = map(int, input().split())
    insert(a, b, d, graph)

start, end = 1, n

pq = []

best_values = [0] * (n+1)
dist = [sys.maxsize] * (n+1)
dist[start] = 0

heapq.heappush(pq, (0, start))
best_values[start] += pick_up[start]

while pq:
    d, u = heapq.heappop(pq)

    if d > dist[u]:
        continue
    
    if u not in graph:
        continue

    for v, w in graph[u]:

        if dist[u] + w < dist[v] or (dist[u] + w == dist[v] and best_values[u]+pick_up[v] > best_values[v]):
            best_values[v] = best_values[u] + pick_up[v]
            dist[v] = dist[u] + w
            heapq.heappush(pq, (dist[v], v))

if dist[end] == sys.maxsize:
    print("impossible")
else:
    print(dist[end], best_values[end])