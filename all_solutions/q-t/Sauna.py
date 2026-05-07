n = int(input())

A, B = 0, float('inf')

for _ in range(n):
    a, b = map(int, input().split())
    A = max(A, a)
    B = min(B, b)

if B-A+1 > 0:
    print(B-A+1, A)
else:
    print("bad news")
