a, b = map(int, input().split(" "))
c = 0
g = [int(x) for x in input().split(" ")]
output = 0
for i in range(b):
    if c + g[i] <= a:
        c += g[i]
    else:
        output = b-i
        break

print(output)