n, m = map(int, input().split(" "))
d = dict()
for i in range(n):
    items = [x for x in input().split(" ")]
    if i == 0:
        for j in range(m):
            d[items[j]]=1
    else:
        for j in range(m):
            if items[j] in d:
                d[items[j]]+=1
sum = 0
output = []
for item in d:
    if d[item] == n:
        sum+=1
        output.append(item)
print(sum)
output.sort()
for item in output:
    print(item)
