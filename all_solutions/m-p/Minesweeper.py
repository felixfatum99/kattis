n, m, k = map(int, input().split(" "))
p = [["."] * m for _ in range(n)] 
for i in range(k):
    x, y = map(int, input().split(" "))
    p[x-1][y-1]="*"
for row in p:
    print("".join(row))

