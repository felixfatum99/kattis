def p(l, moves):
    s = sum([x.count("o") for x in l])
    m = moves
    for j in range(len(l)):
        x = l[j]
        if x.count("o") > 0:
            for i in range(0, len(x), 1):
                if x.count("o") > 1:
                    if i < len(x)-2:
                        if x[i:i+3] == ".oo":
                            l[j] = x[:i]+"o.."+x[i+3:]
                            sc, mc = p(l, moves+1)
                            if sc < s:
                                s = sc
                                m = mc
                            l[j] = x
                        if x[i:i+3] == "oo.":
                            l[j] = x[:i]+"..o"+x[i+3:]
                            sc, mc = p(l, moves+1)
                            if sc < s:
                                s = sc
                                m = mc
                            l[j] = x
                if j>0 and j<4:
                        if x[i] == "o":
                            above = l[j-1]
                            below = l[j+1]
                            if above[i] == "o" and below[i] == ".":
                                l[j-1] = l[j-1][:i]+"."+l[j-1][i+1:]
                                l[j] = l[j][:i]+"."+l[j][i+1:]
                                l[j+1] = l[j+1][:i]+"o"+l[j+1][i+1:]
                                sc, mc = p(l, moves+1)
                                if sc < s:
                                    s = sc
                                    m = mc
                                l[j-1] = above
                                l[j] = x
                                l[j+1] = below
                            if above[i] == "." and below[i] == "o":
                                l[j-1] = l[j-1][:i]+"o"+l[j-1][i+1:]
                                l[j] = l[j][:i]+"."+l[j][i+1:]
                                l[j+1] = l[j+1][:i]+"."+l[j+1][i+1:]
                                sc, mc = p(l, moves+1)
                                if sc < s:
                                    s = sc
                                    m = mc
                                l[j-1] = above
                                l[j] = x
                                l[j+1] = below
    return s, m

n = int(input())
for i in range(n):
    board = []
    if i > 0:
        empty = input()
        
    for j in range(5):
        g = input()
        board.append(g)

    s, m = p(board, 0)
    print(s, m)