n = int(input())
l = [0, 0, 3]
for i in range(n):
    x = int(input())
    l[i] = x
    if i == 0:
        l[1] = x

w = l[0]*2*l[2]
L = (l[1]-2)*2*l[2]
r = (l[1]-2)*(l[0]-2)
print(w+L+r)