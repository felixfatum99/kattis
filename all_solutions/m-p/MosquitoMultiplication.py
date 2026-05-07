import sys

lines = sys.stdin.readlines()

for line in lines:
    M, P, L, E, R, S, N = map(int, line.split())
    
    for _ in range(N):
        old_m = M
        M = 0 if S == 0 else (P - (P%S)) / S 
        P = 0 if R == 0 else (L - (L%R)) / R
        L = old_m * E   
    
    print(int(M))