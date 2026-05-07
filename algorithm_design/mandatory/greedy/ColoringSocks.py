def cs():
    sck = [int(x) for x in input().split(" ")]
    s = sck[0]
    c = sck[1]
    k = sck[2]
    socks = [int(x) for x in input().split(" ")]
    socks.sort()
    
    wm = 0
    m = []

    for i in range(s):
        if len(m) == 0:
            m.append([socks[0]])
            wm+=1
        else:
            inserted = False
            if len(m[wm-1])<c:
                if abs(socks[i]-m[wm-1][0]) <= k:
                    m[wm-1].append(socks[i])
                    inserted = True
            if not inserted:
                m.append([socks[i]])
                wm+=1

    print(wm)
cs()
                