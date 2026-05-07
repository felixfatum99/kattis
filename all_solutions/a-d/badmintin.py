def determine_set(a, b):
    _max = max(a, b)
    _min = min(a, b)

    if a == b and a == 30:
        return "!"
    elif a == 30 and b == 29:
        return "A"
    elif b == 30 and a == 29:
        return "B"
    elif _max > 21 and (_min < 20 or _max-_min > 2):
        return "!"
    elif a == b:
        return  "?"
    elif a < 21 and b < 21:
        return  "?"
    elif _max > 21 and _max-_min != 2:
        return "?"
    elif _max == 21 and _min == 20:
        return "?"
    elif a >= 21 and b < a:
        return "A"
    elif b >= 21 and a < b:
        return "B"
    elif a > 21 and a-b == 2:
        return "A"
    elif b > 21 and b-a == 2:
        return "B"

sets = input().split()
if len(sets) > 3:
    print("!")
else:
    res = ""    
    for set in sets:
        a, b = map(int, set.split("-"))
        r = determine_set(a, b)
        res+=r
    
    if "!" in res:
        print("!")
    elif len(sets) == 1:
        print("?")
    elif len(sets) == 2 and res[0] == "?":
        print("!")
    elif len(sets) == 3 and (res[0] == "?" or res[1] == "?"):
        print("!")
    elif len(sets) == 3 and res[0] == res[1] == res[2]:
        print("!")
    elif len(sets) == 2:
        if res == "AA":
            print("A")
        elif res == "BB":
            print("B")
        else:
            print("?")
    elif len(sets) == 3:
        if res[0] == res[1]:
            print("!")
        elif res.count("A") == 2 and res.count("B") == 1:
            print("A")
        elif res.count("B") == 2 and res.count("A") == 1:
            print("B")
        elif "?" in res:
            print("?")

