t = int(input())

for z in range(t):
    R, k, N = map(int, input().split(" "))
    G = [int(x) for x in input().split(" ")]
    euros = 0
    while R!=0:
        r_sum = k
        for i in range(N):
            if r_sum-G[0]>=0:
                x = G.pop(0)
                r_sum -= x
                euros += x
                G.append(x)
            else:
                break
        R-=1
    print("Case #"+str(z+1)+":", euros)