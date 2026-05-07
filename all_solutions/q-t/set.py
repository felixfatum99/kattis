a, b = map(int, input().split("-"))
_max = max(a, b)
_min = min(a, b)

if a == b and a == 30:
    print("!")
elif a == 30 and b == 29:
    print("A")
elif b == 30 and a == 29:
    print("B")
elif _max > 21 and (_min < 20 or _max-_min > 2):
    print("!")
elif a == b:
    print("?")
elif a < 21 and b < 21:
    print("?")
elif _max > 21 and _max-_min != 2:
    print("?")
elif _max == 21 and _min == 20:
    print("?")
elif a >= 21 and b < a:
    print("A")
elif b >= 21 and a < b:
    print("B")
elif a > 21 and a-b == 2:
    print("A")
elif b > 21 and b-a == 2:
    print("B")