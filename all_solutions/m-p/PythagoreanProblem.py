import math

a, b = map(int, input().split())

c1 = math.sqrt(pow(a, 2) + pow(b, 2))
c2 = math.sqrt(pow(max(a, b),2)-pow(min(a, b), 2))

mi = min(c1, c2)
ma = max(c1, c2)

print(int(mi) if mi.is_integer() else int(ma) if ma.is_integer() else "Pythagoras is sad :(")