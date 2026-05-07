n = int(input())
m = 0
dp = []

def pe():
    z = [-1] * (m+1)
    z[0] = 0

    for v in dp:
        if v[1] != -1:
            for i in range(m, -1, -1):
                if z[i] != -1:
                    if z[i+v[0]] != -1:
                        z[i+v[0]] = min(z[i+v[0]], z[i]+v[1])
                    else:
                        z[i+v[0]] = z[i]+v[1]
                    if i == v[0]:
                        z[i] = min(v[1], z[i])
                elif i == v[0]:
                    z[i] = v[1]
    return z

for i in range(n):
    d, c, f, u = map(int, input().split(" "))
    m+=d
    diff = abs(c-f)
    tv = c + f + u
    vn = max(0, (tv // 2 + 1) - c)

    if vn > u:
        dp.append((d, -1))
    else:
        dp.append((d, vn))

list = pe()

p = False
M = float("inf")
for i in range(len(list)):
    if list[i] != -1 and i > m-i:
        p = True
        M = min(M, int(list[i]))
if not p:
    print("impossible")
else:
    print(M)