import math
a, b = map(int, input().split())
p = True

for i in range(int(input())):
    x, y = map(int, input().split())
    if math.sqrt(abs(a-x)**2+abs(b-y)**2) < 8:
        print("NO")
        p = False

if p:
    print("YES")
