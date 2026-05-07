# Ford-Fulkerson algorith in Python

from collections import defaultdict


class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    def searching_algo_BFS(self, s, t, parent):

        visited = [False] * (self.ROW)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:

            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0

        while self.searching_algo_BFS(source, sink, parent):

            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


graph = [[0, 25, 9, 0, 0, 0, 0],
         [25, 0, 0, 13, 0, 0, 0],
         [9, 0, 0, 17, 0, 0, 0],
         [0, 13, 17, 0, 11, 7, 0],
         [0, 0, 0, 11, 0, 0, 19],
         [0, 0, 0, 7, 0, 0, 23],
         [0, 0, 0, 0, 19, 23, 0]]

g = Graph(graph)

source = 0
sink = 6

print(g.ford_fulkerson(source, sink))