a, b = map(int, input().split())

id = [int(x) for x in range(a)]

for i in range(b):
    x, y = map(int, input().split())

    val_x, val_y = id[x], id[y]
    min_val = min(val_x, val_y)
    max_val = max(val_x, val_y)

    for i in range(a):
        if id[i] == max_val:
            id[i] = min_val

print(" ".join([str(ID) for ID in id]))
