import math
p, d = map(int, input().split(" "))
l = []
for i in range(d):
    l.append([0, 0])
v = 0
for i in range(p):
    di, A, B = map(int, input().split(" "))
    l[di-1][0] += A
    l[di-1][1] += B
    v+= (A+B)

wa = 0
wb = 0

for i in range(d):
    a = l[i][0]
    b = l[i][1]
    t = (math.floor((a+b)/2))+1
    if a > b:
        print("A",a-t, b)
        wa+=a-t
        wb+=b
    else:
        print("B", a, b-t)
        wb+=b-t
        wa+=a
print((abs(wa-wb)/v))