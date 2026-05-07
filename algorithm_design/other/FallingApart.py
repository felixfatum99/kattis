n = int(input())
l = [int(x) for x in input().split(" ")]
l.sort(reverse=True)
a = 0
b = 0
for i in range(n):
    if i % 2 == 0:
        a += l[i]
    else:
        b+= l[i]
print(a, b)