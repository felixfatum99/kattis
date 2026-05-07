T = int(input())

for c in range(T):
    n = int(input())
    p1 = input().split()

    n2 = int(input())
    p2 = input().split()

    print(n+n2)
    res = [0 for _ in range(n+n2+1)]
    for j in range(len(p1)):
        for k in range(len(p2)):
            res[j+k] += int(p1[j])*int(p2[k])
    print(*res)




