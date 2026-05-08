#https://open.kattis.com/problems/1dfroggereasy
n, s, m = map(int, input().split())
board = list(map(int, input().split()))
visited = set()
hops = 0

pos = s - 1

while True:
    if board[pos] == m:
        print("magic")
        print(hops)
        break

    visited.add(pos)

    jump = board[pos]
    next_pos = pos + jump

    if next_pos < 0:
        print("left")
        print(hops + 1)
        break
    if next_pos >= n:
        print("right")
        print(hops + 1)
        break

    if next_pos in visited:
        print("cycle")
        print(hops + 1)
        break

    pos = next_pos
    hops += 1