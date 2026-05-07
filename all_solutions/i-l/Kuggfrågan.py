def count(n, s, m, board):
    s = s
    m = m
    n = n
    board = board
    hops = 0
    visited = set()
    output = 0
    while True:
        if board[s-1] == m:
            output = 1
            break
        
        if s+board[s-1] < 0 or s+board[s-1] > n or s-1+board[s-1] in visited:
            break

        s += board[s-1]
        visited.add(s-1)
        hops+=1
    
    return output

s = int(input())
numbers = [int(x) for x in input().split()]
output = 0
for i in range(s):
    for j in range(s):
        output += (count(s, i+1, numbers[j], numbers))

print(output)