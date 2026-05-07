import math
a = float(input())
b = float(input())
c = float(input())

cur = 2 * math.pi * (a/2)
if cur >= b*c:
    print("YES")
else:
    print("NO")
