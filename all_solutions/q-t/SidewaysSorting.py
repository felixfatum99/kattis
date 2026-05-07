while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    
    d = {}
    n = []
    for i in range(a):
        s = input()
        for j in range(b):
            if i == 0:
                n.append(s[j])
            else:
                n[j] += s[j]

    for i in range(len(n)):
        d[n[i].lower()] = n[i]
        n[i] = n[i].lower() 
    n.sort()

    for i in range(a):
        for j in range(b):
            if j == b-1:
                print(d[n[j]][i])
            else:
                print(d[n[j]][i], end="")

