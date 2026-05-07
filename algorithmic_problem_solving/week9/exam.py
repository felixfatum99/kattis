c, m, f = int(input()), input(), input()
s, l = 0, len(m)

for i in range(l):
    if m[i] == f[i]:
        s += 1

print(l -  abs(c - s))