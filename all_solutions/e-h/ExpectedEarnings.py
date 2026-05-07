a, b, c = map(str, input().split())
a = int(a)
b = int(b)
c = float(c)

if c * a >= b:
    print("Spela inte!")
else:
    print("spela")