import sys

def dp(items, value):
    res = []
    for i in range(value+1):
        res.append([(0, i)])

    for item in items:
        for i in range(value, 0, -1):
            if i%item == 0:
                res[i].append((item, i/item))
                res[i][0] = (res[i][0][0]+1, res[i][0][1])
            if (res[i][0][0] > 0 and i+item <= value):
                for j in range(res[i][0][0]):
                    if res[i][j+1][0] == item:
                        continue
                    m = 1
                    while True:
                        if (m*item)+i <= value:
                            result = (res[i][j+1], (item, m))
                            res[i+(item*m)].append(result)
                            res[i+(item*m)][0] = (res[i+(item*m)][0][0]+1, res[i+(item*m)][0][1])
                            m+=1
                        else:
                            break
                
    return res[value]
n = int(input())
items = [int(x) for x in input().split(" ")]
itemss = sorted(items, reverse=True)
a = int(input())
o = [int(x) for x in input().split(" ")]

for i in o:
    res = dp(itemss, i)
    if res[0][0] > 1:
        print("Ambiguous")
    elif res[0][0] == 0:
        print("Impossible")
    else:
        values = []
        contains_tuple = any(isinstance(element, tuple) for element in res[1])
        if contains_tuple:
            for j in range(0, len(res[1]), 1):
                for i in range(len(items)):
                    t = res[1][j][0]
                    l = int(res[1][j][1])
                    if t == items[i]:
                        for x in range(l):
                            values.append(str(i+1))
        else:
            t = res[1][0]
            l = int(res[1][1])
            for i in range(len(items)):
                if t == items[i]:
                        for x in range(l):
                            values.append(str(i+1))
        values.sort()
        print(' '.join(values))


