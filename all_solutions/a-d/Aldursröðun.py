import math
import bisect

n = int(input())
numbers = [int(x) for x in input().split()]
d = {}


for n in numbers:
    list = {}
    for k in d.keys():
        if math.gcd(n, k) > 1:
            list[k] = 1
            d[k][n] = 1
    d[n] = list


can_work = True
start = None
end = None
for k in d.keys():
    if len(d[k]) == 1:
        if start == None:
            start = k
        elif end == None:
            end = k
        else:
            can_work = False
    elif len(d[k]) == 0:
        can_work = False


def find_path(d):
    # Find a starting node (any vertex with only one connection, a natural endpoint)
    start = next((k for k in d if len(d[k]) == 1), None)
    if not start:
        return None  # No path possible if no endpoint is found

    path = []
    visited = set()

    def dfs(node):
        path.append(node)
        visited.add(node)
        # Move to the next unvisited neighbor
        for neighbor in d[node]:
            if neighbor not in visited:
                dfs(neighbor)
        return path

    # Call DFS from the starting node
    full_path = dfs(start)
    
    # Verify the path covers all nodes and all connections are used in sequence
    if len(visited) == len(d):
        for i in range(len(full_path) - 1):
            if full_path[i + 1] not in d[full_path[i]]:
                return None  # Return None if any consecutive nodes are not connected
        return full_path
    else:
        return None  # No Hamiltonian path exists

# Usage
path = find_path(d)
if path:
    print(" ".join(map(str, path)))  # Convert each int to string and join with space
else:
    print("No path exists that uses all vertices.")