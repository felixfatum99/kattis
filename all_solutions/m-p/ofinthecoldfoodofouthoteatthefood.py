t, h = map(int, input().split())
if h <= 2 * t:
    print(t + h / 2)
else:
    print((2 * t * h) ** 0.5)

