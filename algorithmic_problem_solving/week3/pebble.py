def p(l):
    s = l.count("o")
    for i in range(0, len(l)-2, 1):
        if l[i:i+3] == "-oo":
            s = min(s, p(l[:i]+"o--"+l[i+3:]))
        if l[i:i+3] == "oo-":
            s = min(s, p(l[:i]+"--o"+l[i+3:]))
    return s

n = int(input())
for i in range(n):
    g = input()
    print(p(g))