import sys
input = sys.stdin.buffer.readline

def solve(y):
    global count
    if y == N:
        count += 1
        return
    for x in range(N):
        if (column[x] or diag1[x+y] or diag2[x-y+N-1]) or (y, x) in holes:
            continue
        column[x] = diag1[x+y] = diag2[x-y+N-1] = True
        solve(y+1)
        column[x] = diag1[x+y] = diag2[x-y+N-1] = False

while True:
    N, M = map(int, input().split())

    if N == 0 and M == 0:
        break
    
    column = [False]*N
    diag1 = [False]*((N*2)-1)
    diag2 = [False]*((N*2)-1)
    holes = [tuple(map(int, input().split())) for _ in range(M)]

    count = 0
    solve(0)
    print(count)