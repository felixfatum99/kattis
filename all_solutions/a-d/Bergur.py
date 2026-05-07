N = int(input())
T = [int(x) for x in input().split()]

for i in range(N-2, -1, -1):
    T[i] = min(T[i+1], T[i])

print(sum(T))