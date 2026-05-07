i = int(input())

l = [int(x) for x in input().split(" ")]

for j in range(i):
    l.append(,j)

l.sort()
res = []
if i == 1:
    print(1)
else:
    for i in range(len(l)):
        if i == 0:
            if l[i][0] != l[i+1]:
                res.append(l[i])
        elif i == len(l)-1:
            if l[i][0] != l[i-1]:
                res.append(l[i])
        else:
            if l[i][0] != l[i+1] and l[i][0] != l[i-1]:
                res.append(l[i])
    if len(res)==0:
        print("none")
    else:
        res.sort()
        print(res[len(res)-1][1])
