k = int(input())
sorted = []
nonsorted = []

for i in range(k):
    c = int(input())
    sorted.append(c)
    nonsorted.append(c)

sorted.sort()
sum = 0
cc = nonsorted.pop(0)
while cc!=0:
    sum += 1
    for i in range(len(sorted)):
        if cc == sorted[i]:
            if nonsorted:
                cc = nonsorted.pop(0)
            else:
                cc = 0
print(sum)