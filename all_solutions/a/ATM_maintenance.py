#https://open.kattis.com/problems/atmmaintenance
a, b = map(int, input().split())
p = [int(x) for x in input().split()]

for l in p:
    if l <= b:
        b -= l
        print(1, end="")
    else:
        print(0, end="")