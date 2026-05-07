r, c = map(int, input().split())


route = 1
for i in range(r):
    word = input()
    if route % 2 == 0:
        #l < r
        s = c-len(word)
        l = 0 if s == 0 else int(s / 2) if s % 2 == 0 else int((s+1) / 2)
        r = 0 if s == 0 else int(s / 2) if s % 2 == 0 else int((s-1) / 2)
        if l != r:
            route += 1
        print(l*"."+word+r*".")
    else:
        #r < l
        s = c-len(word)
        l = 0 if s == 0 else int(s / 2) if s % 2 == 0 else int((s-1) / 2)
        r = 0 if s == 0 else int(s / 2) if s % 2 == 0 else int((s+1) / 2)
        if l != r:
            route += 1
        print(l*"."+word+r*".")
