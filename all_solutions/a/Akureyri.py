#https://open.kattis.com/problems/akureyri
n = {}

for i in range(int(input())):
    input()
    c = input()
    if c in n:
        n[c] += 1
    else:
        n[c] = 1

for c in n:
    print(c, n[c])