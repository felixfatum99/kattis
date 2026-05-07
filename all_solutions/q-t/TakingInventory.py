i = dict()
for _ in range(int(input())):
    name, size = map(str, input().split())
    if name in i:
        i[name] += int(size)
    else:
       i[name] = int(size)

for key in i:
    if i[key] <= 64:
        print(key, 1)
    else:
        rest = i[key] % 64
        total_fill = ((i[key]-rest)/64)
        if rest > 0:
            total_fill += 1
        print(key, int(total_fill))
        
